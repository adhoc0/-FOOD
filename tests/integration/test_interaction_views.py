"""Yorum, puan ve favori view davranış testleri."""

import pytest
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from interactions.models import Comment, Rating
from recipes.models import Recipe
from tests.factories import RatingFactory, RecipeFactory, UserFactory

CONTENT = "Harika bir tarif, herkese öneririm."


def _post_comment(client, recipe, **data):
    return client.post(
        reverse("interactions:add_comment", kwargs={"recipe_id": recipe.pk}),
        data,
    )


def _messages(response):
    return [str(message) for message in get_messages(response.wsgi_request)]


@pytest.fixture
def logged_in_client():
    client = Client()
    user = UserFactory()
    client.force_login(user)
    client.user = user
    return client


@pytest.mark.django_db
class TestAddCommentView:
    def test_empty_submission_shows_error_and_creates_nothing(self, logged_in_client):
        recipe = RecipeFactory()

        response = _post_comment(logged_in_client, recipe)

        assert response.status_code == 302
        assert "Yorum yazın veya puan verin." in _messages(response)
        assert Comment.objects.count() == 0
        assert Rating.objects.count() == 0

    def test_score_only_submission_saves_rating(self, logged_in_client):
        recipe = RecipeFactory()

        response = _post_comment(logged_in_client, recipe, score="4")

        assert response.status_code == 302
        assert Rating.objects.get(user=logged_in_client.user, recipe=recipe).score == 4
        assert "Puanınız kaydedildi." in _messages(response)

    def test_out_of_range_score_is_reported_without_server_error(self, logged_in_client):
        recipe = RecipeFactory()

        response = _post_comment(logged_in_client, recipe, score="9")

        assert response.status_code == 302
        assert Rating.objects.count() == 0
        assert "Puan 1 ile 5 arasında olmalıdır." in _messages(response)

    @pytest.mark.parametrize("score", ["abc", "-1", "4.5"])
    def test_non_numeric_score_is_reported(self, logged_in_client, score):
        recipe = RecipeFactory()

        response = _post_comment(logged_in_client, recipe, score=score)

        assert Rating.objects.count() == 0
        assert "Puan geçerli bir sayı olmalıdır." in _messages(response)

    def test_comment_and_score_can_be_sent_together(self, logged_in_client):
        recipe = RecipeFactory()

        _post_comment(logged_in_client, recipe, content=CONTENT, score="5")

        assert Comment.objects.filter(recipe=recipe, is_approved=False).count() == 1
        assert Rating.objects.filter(recipe=recipe, score=5).count() == 1

    def test_invalid_comment_does_not_block_rating(self, logged_in_client):
        recipe = RecipeFactory()

        _post_comment(logged_in_client, recipe, content="x", score="3")

        assert Comment.objects.count() == 0
        assert Rating.objects.filter(recipe=recipe, score=3).count() == 1


@pytest.mark.django_db
class TestRatingStatistics:
    def test_statistics_reflect_all_ratings(self, logged_in_client):
        recipe = RecipeFactory()
        RatingFactory(recipe=recipe, score=2)

        _post_comment(logged_in_client, recipe, score="4")

        recipe.refresh_from_db()
        assert recipe.rating_count == 2
        assert float(recipe.average_rating) == 3.0

    def test_deleting_a_rating_refreshes_statistics(self):
        recipe = RecipeFactory()
        rating = RatingFactory(recipe=recipe, score=5)
        recipe.refresh_from_db()
        assert recipe.rating_count == 1

        rating.delete()

        recipe.refresh_from_db()
        assert recipe.rating_count == 0
        assert float(recipe.average_rating) == 0.0


@pytest.mark.django_db
class TestFavoriteCounter:
    def test_toggle_twice_returns_counter_to_zero(self, logged_in_client):
        recipe = RecipeFactory()
        url = reverse("interactions:toggle_favorite", kwargs={"recipe_id": recipe.pk})

        logged_in_client.post(url)
        assert Recipe.objects.get(pk=recipe.pk).favorite_count == 1

        logged_in_client.post(url)
        assert Recipe.objects.get(pk=recipe.pk).favorite_count == 0


# ─────────────────────────────────────────────
# JSON (fetch) yanıtları — ilerleyici geliştirme
# ─────────────────────────────────────────────
JSON = {"HTTP_ACCEPT": "application/json"}


@pytest.mark.django_db
class TestInteractionJsonResponses:
    def test_favorite_toggle_returns_state_without_flash_message(self, logged_in_client):
        recipe = RecipeFactory()
        url = reverse("interactions:toggle_favorite", kwargs={"recipe_id": recipe.pk})

        added = logged_in_client.post(url, **JSON)
        assert added.status_code == 200
        assert added.json()["favorited"] is True
        assert added.json()["messages"][0]["level"] == "success"
        assert _messages(added) == []

        removed = logged_in_client.post(url, **JSON)
        assert removed.json()["favorited"] is False
        assert removed.json()["messages"][0]["level"] == "info"

    def test_rating_returns_updated_summary(self, logged_in_client):
        recipe = RecipeFactory()
        RatingFactory(recipe=recipe, score=2)

        response = logged_in_client.post(
            reverse("interactions:add_comment", kwargs={"recipe_id": recipe.pk}),
            {"score": "4"},
            **JSON,
        )

        data = response.json()
        assert response.status_code == 200
        assert data["ok"] is True
        assert data["rating_count"] == 2
        assert data["average_rating"] == "3.0"

    def test_comment_returns_pending_message(self, logged_in_client):
        recipe = RecipeFactory()

        response = logged_in_client.post(
            reverse("interactions:add_comment", kwargs={"recipe_id": recipe.pk}),
            {"content": CONTENT},
            **JSON,
        )

        assert response.json()["ok"] is True
        assert Comment.objects.filter(recipe=recipe).count() == 1

    def test_invalid_submission_returns_400(self, logged_in_client):
        recipe = RecipeFactory()

        empty = logged_in_client.post(
            reverse("interactions:add_comment", kwargs={"recipe_id": recipe.pk}), **JSON
        )
        bad_score = logged_in_client.post(
            reverse("interactions:add_comment", kwargs={"recipe_id": recipe.pk}),
            {"score": "abc"},
            **JSON,
        )

        assert empty.status_code == 400
        assert empty.json()["ok"] is False
        assert bad_score.status_code == 400
        assert not Rating.objects.filter(recipe=recipe).exists()

    def test_partial_success_returns_200_with_both_messages(self, logged_in_client):
        recipe = RecipeFactory()

        response = logged_in_client.post(
            reverse("interactions:add_comment", kwargs={"recipe_id": recipe.pk}),
            {"content": CONTENT, "score": "9"},
            **JSON,
        )

        levels = {item["level"] for item in response.json()["messages"]}
        assert response.status_code == 200
        assert levels == {"success", "error"}

    def test_anonymous_json_request_is_redirected_to_login(self):
        recipe = RecipeFactory()

        response = Client().post(
            reverse("interactions:toggle_favorite", kwargs={"recipe_id": recipe.pk}), **JSON
        )

        assert response.status_code == 302
        assert reverse("accounts:login") in response["Location"]


@pytest.mark.django_db
def test_detail_page_shows_favorite_state(logged_in_client):
    recipe = RecipeFactory()
    url = reverse("recipes:recipe_detail", kwargs={"slug": recipe.slug})

    assert "Favorilerime ekle" in logged_in_client.get(url).content.decode()

    logged_in_client.post(
        reverse("interactions:toggle_favorite", kwargs={"recipe_id": recipe.pk})
    )
    page = logged_in_client.get(url).content.decode()
    assert "Favorilerimden çıkar" in page
    assert 'aria-pressed="true"' in page
