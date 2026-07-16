"""
Service unit tests.

RecipeService, FavoriteService, RatingService, SearchService testleri.
Veritabanı erişimi gerektirir (pytest-django).
"""

import pytest
from django.core.exceptions import ValidationError

from recipes.choices import Status
from recipes.services import FavoriteService, RatingService, RecipeService
from tests.factories import (
    CategoryFactory,
    FavoriteFactory,
    ProvinceFactory,
    RatingFactory,
    RecipeFactory,
    UserFactory,
)


@pytest.mark.django_db
class TestRecipeServiceCreate:
    """RecipeService.create testleri."""

    def test_create_recipe(self):
        user = UserFactory()
        province = ProvinceFactory()
        category = CategoryFactory()

        recipe = RecipeService.create(
            title="Test Tarifi",
            slug="test-tarifi",
            province=province,
            category=category,
            author=user,
            summary="A" * 50,
            instructions="A" * 100,
            preparation_time=15,
            cooking_time=30,
            servings=4,
        )

        assert recipe.pk is not None
        assert recipe.title == "Test Tarifi"
        assert recipe.status == Status.DRAFT


@pytest.mark.django_db
class TestRecipeServicePublish:
    """RecipeService.publish / unpublish testleri."""

    def test_publish_recipe(self):
        recipe = RecipeFactory(status=Status.DRAFT, published_at=None)
        result = RecipeService.publish(recipe)

        assert result.status == Status.PUBLISHED
        assert result.published_at is not None

    def test_unpublish_recipe(self):
        recipe = RecipeFactory(status=Status.PUBLISHED)
        result = RecipeService.unpublish(recipe)

        assert result.status == Status.DRAFT
        assert result.published_at is None


@pytest.mark.django_db
class TestRecipeServiceFeature:
    """RecipeService.feature / unfeature testleri."""

    def test_feature_recipe(self):
        recipe = RecipeFactory(is_featured=False)
        result = RecipeService.feature(recipe)
        assert result.is_featured is True

    def test_unfeature_recipe(self):
        recipe = RecipeFactory(is_featured=True)
        result = RecipeService.unfeature(recipe)
        assert result.is_featured is False


@pytest.mark.django_db
class TestRecipeServiceViewCount:
    """RecipeService.increment_view_count testleri."""

    def test_increment_view_count(self):
        recipe = RecipeFactory(view_count=0)
        RecipeService.increment_view_count(recipe)
        recipe.refresh_from_db()
        assert recipe.view_count == 1

    def test_increment_view_count_multiple(self):
        recipe = RecipeFactory(view_count=5)
        RecipeService.increment_view_count(recipe)
        recipe.refresh_from_db()
        assert recipe.view_count == 6


@pytest.mark.django_db
class TestRecipeServiceDelete:
    """RecipeService.delete testleri."""

    def test_delete_recipe(self):
        recipe = RecipeFactory()
        recipe_pk = recipe.pk
        RecipeService.delete(recipe)

        from recipes.models import Recipe

        assert not Recipe.objects.filter(pk=recipe_pk).exists()


# ─────────────────────────────────────────────
# FavoriteService
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestFavoriteService:
    """FavoriteService testleri."""

    def test_toggle_adds_favorite(self):
        user = UserFactory()
        recipe = RecipeFactory(favorite_count=0)

        result = FavoriteService.toggle(user, recipe)

        assert result is True
        recipe.refresh_from_db()
        assert recipe.favorite_count == 1

    def test_toggle_removes_favorite(self):
        user = UserFactory()
        recipe = RecipeFactory(favorite_count=1)
        FavoriteFactory(user=user, recipe=recipe)

        result = FavoriteService.toggle(user, recipe)

        assert result is False
        recipe.refresh_from_db()
        assert recipe.favorite_count == 0

    def test_is_favorited_true(self):
        user = UserFactory()
        recipe = RecipeFactory()
        FavoriteFactory(user=user, recipe=recipe)

        assert FavoriteService.is_favorited(user, recipe) is True

    def test_is_favorited_false(self):
        user = UserFactory()
        recipe = RecipeFactory()

        assert FavoriteService.is_favorited(user, recipe) is False

    def test_get_user_favorites(self):
        user = UserFactory()
        recipe1 = RecipeFactory()
        recipe2 = RecipeFactory()
        FavoriteFactory(user=user, recipe=recipe1)
        FavoriteFactory(user=user, recipe=recipe2)

        favorites = FavoriteService.get_user_favorites(user)
        assert favorites.count() == 2


# ─────────────────────────────────────────────
# RatingService
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestRatingService:
    """RatingService testleri."""

    def test_rate_creates_rating(self):
        user = UserFactory()
        recipe = RecipeFactory()

        rating = RatingService.rate(user, recipe, 5)

        assert rating.score == 5
        assert rating.user == user

    @pytest.mark.parametrize("score", [0, 6, "5"])
    def test_rate_rejects_invalid_score(self, score):
        user = UserFactory()
        recipe = RecipeFactory()

        with pytest.raises(ValidationError):
            RatingService.rate(user, recipe, score)

    def test_rate_updates_existing(self):
        user = UserFactory()
        recipe = RecipeFactory()
        RatingFactory(user=user, recipe=recipe, score=3)

        rating = RatingService.rate(user, recipe, 5)

        assert rating.score == 5
        from interactions.models import Rating

        assert Rating.objects.filter(user=user, recipe=recipe).count() == 1

    def test_get_average_rating(self):
        recipe = RecipeFactory()
        RatingFactory(recipe=recipe, score=4)
        RatingFactory(recipe=recipe, score=2)

        average = RatingService.get_average_rating(recipe)

        assert average == 3.0

    def test_get_average_rating_no_ratings(self):
        recipe = RecipeFactory()
        average = RatingService.get_average_rating(recipe)
        assert average == 0

    def test_get_user_rating(self):
        user = UserFactory()
        recipe = RecipeFactory()
        RatingFactory(user=user, recipe=recipe, score=4)

        result = RatingService.get_user_rating(user, recipe)
        assert result == 4

    def test_get_user_rating_none(self):
        user = UserFactory()
        recipe = RecipeFactory()

        result = RatingService.get_user_rating(user, recipe)
        assert result is None

    def test_get_rating_count(self):
        recipe = RecipeFactory()
        RatingFactory(recipe=recipe)
        RatingFactory(recipe=recipe)

        assert RatingService.get_rating_count(recipe) == 2
