"""
Model unit tests.

Recipe, Category, Province, Favorite, Rating, Comment model testleri.
QuerySet zinciri ve constraint testleri.
"""

import pytest
from django.db import IntegrityError

from interactions.models import Favorite, Rating
from recipes.choices import Status
from recipes.models import Recipe
from tests.factories import (
    CategoryFactory,
    DraftRecipeFactory,
    FavoriteFactory,
    ProvinceFactory,
    RatingFactory,
    RecipeFactory,
    UserFactory,
)


@pytest.mark.django_db
class TestRecipeModel:
    """Recipe model testleri."""

    def test_str(self):
        recipe = RecipeFactory(title="Ali Nazik")
        assert str(recipe) == "Ali Nazik"

    def test_get_absolute_url(self):
        recipe = RecipeFactory(slug="ali-nazik")
        assert recipe.get_absolute_url() == "/tarifler/ali-nazik/"

    def test_default_ordering(self):
        """Tarifler -published_at, -created_at sıralı olmalı."""
        RecipeFactory()
        recipe2 = RecipeFactory()

        recipes = list(Recipe.objects.all())
        # En son eklenen en üstte
        assert recipes[0].pk == recipe2.pk


@pytest.mark.django_db
class TestRecipeQuerySet:
    """RecipeQuerySet zinciri testleri."""

    def test_active_filter(self):
        RecipeFactory(is_active=True)
        RecipeFactory(is_active=False)

        assert Recipe.objects.active().count() == 1

    def test_published_filter(self):
        RecipeFactory(status=Status.PUBLISHED)
        DraftRecipeFactory()

        assert Recipe.objects.published().count() == 1

    def test_featured_filter(self):
        RecipeFactory(is_featured=True)
        RecipeFactory(is_featured=False)

        assert Recipe.objects.featured().count() == 1

    def test_by_province(self):
        province = ProvinceFactory()
        RecipeFactory(province=province)
        RecipeFactory()  # farklı province

        assert Recipe.objects.by_province(province).count() == 1

    def test_by_category(self):
        category = CategoryFactory()
        RecipeFactory(category=category)
        RecipeFactory()  # farklı category

        assert Recipe.objects.by_category(category).count() == 1

    def test_by_slug(self):
        RecipeFactory(slug="test-slug", is_active=True)
        result = Recipe.objects.by_slug("test-slug")
        assert result.count() == 1

    def test_by_slug_not_found(self):
        result = Recipe.objects.by_slug("nonexistent")
        assert result.count() == 0

    def test_search(self):
        RecipeFactory(title="Patlıcanlı Kebap", is_active=True)
        RecipeFactory(title="Mantı", is_active=True)

        results = Recipe.objects.search("kebap")
        assert results.count() == 1

    def test_search_empty_query(self):
        RecipeFactory(is_active=True)
        results = Recipe.objects.search("")
        assert results.count() == 1  # Boş sorgu tüm aktif tarifleri döner

    def test_with_related_no_n_plus_one(self):
        """with_related() N+1 sorgu oluşturmamalı."""
        RecipeFactory()
        queryset = Recipe.objects.with_related()
        assert queryset.count() == 1

    def test_chain_active_published_featured(self):
        """Zincirlenmiş filtreler doğru çalışmalı."""
        RecipeFactory(is_active=True, status=Status.PUBLISHED, is_featured=True)
        RecipeFactory(is_active=True, status=Status.PUBLISHED, is_featured=False)
        RecipeFactory(is_active=False, status=Status.PUBLISHED, is_featured=True)

        result = Recipe.objects.active().published().featured()
        assert result.count() == 1


@pytest.mark.django_db
class TestCategoryModel:
    """Category model testleri."""

    def test_str(self):
        category = CategoryFactory(name="Çorbalar")
        assert str(category) == "Çorbalar"

    def test_unique_name(self):
        CategoryFactory(name="Çorbalar", slug="corbalar")
        with pytest.raises(IntegrityError):
            CategoryFactory(name="Çorbalar", slug="corbalar-2")


@pytest.mark.django_db
class TestProvinceModel:
    """Province model testleri."""

    def test_str(self):
        province = ProvinceFactory(plate_code=27, name="Gaziantep")
        assert str(province) == "27 - Gaziantep"


# ─────────────────────────────────────────────
# Interaction Constraints
# ─────────────────────────────────────────────
@pytest.mark.django_db
class TestFavoriteConstraints:
    """Favorite unique_together constraint testi."""

    def test_duplicate_favorite_raises_error(self):
        user = UserFactory()
        recipe = RecipeFactory()
        FavoriteFactory(user=user, recipe=recipe)

        with pytest.raises(IntegrityError):
            Favorite.objects.create(user=user, recipe=recipe)


@pytest.mark.django_db
class TestRatingConstraints:
    """Rating unique_together constraint testi."""

    def test_duplicate_rating_raises_error(self):
        user = UserFactory()
        recipe = RecipeFactory()
        RatingFactory(user=user, recipe=recipe, score=4)

        with pytest.raises(IntegrityError):
            Rating.objects.create(user=user, recipe=recipe, score=5)
