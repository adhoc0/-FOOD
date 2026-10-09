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
