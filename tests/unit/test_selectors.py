"""
Selector unit tests.

RecipeSelector, CategorySelector testleri.
"""

import pytest

from recipes.choices import Status
from recipes.selectors import CategorySelector, RecipeSelector
from tests.factories import (
    CategoryFactory,
    DraftRecipeFactory,
    ProvinceFactory,
    RecipeFactory,
)


@pytest.mark.django_db
class TestRecipeSelector:
    """RecipeSelector testleri."""

    def test_get_published_list(self):
        RecipeFactory(status=Status.PUBLISHED, is_active=True)
        DraftRecipeFactory()

        result = RecipeSelector.get_published_list()
        assert result.count() == 1

    def test_get_recipe_detail_found(self):
        recipe = RecipeFactory(slug="test-detail", is_active=True)
        result = RecipeSelector.get_recipe_detail("test-detail")
        assert result is not None
        assert result.pk == recipe.pk

    def test_get_recipe_detail_not_found(self):
        result = RecipeSelector.get_recipe_detail("nonexistent")
        assert result is None

    def test_get_featured(self):
        RecipeFactory(is_featured=True, status=Status.PUBLISHED, is_active=True)
        RecipeFactory(is_featured=False, status=Status.PUBLISHED, is_active=True)

        result = RecipeSelector.get_featured()
        assert result.count() == 1

    def test_get_by_province(self):
        province = ProvinceFactory()
        RecipeFactory(province=province, status=Status.PUBLISHED, is_active=True)
        RecipeFactory(status=Status.PUBLISHED, is_active=True)  # farklı province

        result = RecipeSelector.get_by_province(province)
        assert result.count() == 1

    def test_get_by_category(self):
        category = CategoryFactory()
        RecipeFactory(category=category, status=Status.PUBLISHED, is_active=True)
        RecipeFactory(status=Status.PUBLISHED, is_active=True)  # farklı category

        result = RecipeSelector.get_by_category(category)
        assert result.count() == 1

    def test_get_related_recipes(self):
        province = ProvinceFactory()
        recipe = RecipeFactory(
            province=province, status=Status.PUBLISHED, is_active=True
        )
        RecipeFactory(
            province=province, status=Status.PUBLISHED, is_active=True
        )  # aynı il
        RecipeFactory(status=Status.PUBLISHED, is_active=True)  # farklı il

        result = RecipeSelector.get_related_recipes(recipe)
        # Aynı ildeki diğer tarif (kendisi hariç)
        assert result.count() == 1

    def test_get_published_count(self):
        RecipeFactory(status=Status.PUBLISHED, is_active=True)
        RecipeFactory(status=Status.PUBLISHED, is_active=True)
        DraftRecipeFactory()

        assert RecipeSelector.get_published_count() == 2


@pytest.mark.django_db
class TestCategorySelector:
    """CategorySelector testleri."""

    def test_get_all_active(self):
        CategoryFactory(is_active=True)
        CategoryFactory(is_active=False)

        result = CategorySelector.get_all_active()
        assert result.count() == 1

    def test_get_by_slug_found(self):
        CategoryFactory(slug="corbalar", is_active=True)
        result = CategorySelector.get_by_slug("corbalar")
        assert result is not None
        assert result.slug == "corbalar"

    def test_get_by_slug_not_found(self):
        result = CategorySelector.get_by_slug("nonexistent")
        assert result is None

    def test_get_with_recipe_count(self):
        category = CategoryFactory(is_active=True)
        RecipeFactory(
            category=category,
            status=Status.PUBLISHED,
            is_active=True,
        )
        RecipeFactory(
            category=category,
            status=Status.PUBLISHED,
            is_active=True,
        )

        result = list(CategorySelector.get_with_recipe_count())
        assert len(result) == 1
        assert result[0].recipe_count == 2
