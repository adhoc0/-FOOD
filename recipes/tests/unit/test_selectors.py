"""RecipeSelector.search_published ve sıralama testleri."""

import pytest
from django.db import connection
from django.test.utils import CaptureQueriesContext

from recipes.choices import Difficulty
from recipes.models import Recipe
from recipes.selectors import RecipeSelector
from tests.factories import (
    CategoryFactory,
    DraftRecipeFactory,
    ProvinceFactory,
    RecipeFactory,
)


@pytest.mark.django_db
class TestSearchPublished:
    def test_returns_only_published_active_recipes(self):
        published = RecipeFactory(title="Çorba A")
        DraftRecipeFactory(title="Çorba B")
        RecipeFactory(title="Çorba C", is_active=False)

        assert list(RecipeSelector.search_published()) == [published]

    def test_filters_by_title_case_insensitively_and_trims_query(self):
        match = RecipeFactory(title="Ali Nazik")
        RecipeFactory(title="Mantı")

        assert list(RecipeSelector.search_published(query="  ALI nazik ")) == [match]

    def test_filters_by_province_category_and_difficulty(self):
        province = ProvinceFactory()
        category = CategoryFactory()
        match = RecipeFactory(
            province=province, category=category, difficulty=Difficulty.EASY
        )
        RecipeFactory(province=province, category=category, difficulty=Difficulty.HARD)
        RecipeFactory(category=category, difficulty=Difficulty.EASY)

        result = RecipeSelector.search_published(
            province_slug=province.slug,
            category_slug=category.slug,
            difficulty=Difficulty.EASY,
        )

        assert list(result) == [match]

    def test_applies_requested_ordering(self):
        low = RecipeFactory(title="Bbb", average_rating=2, rating_count=1)
        high = RecipeFactory(title="Aaa", average_rating=5, rating_count=1)

        assert list(RecipeSelector.search_published(ordering="rating")) == [high, low]
        assert list(RecipeSelector.search_published(ordering="title")) == [high, low]

    def test_unknown_ordering_falls_back_to_latest(self):
        older = RecipeFactory()
        newer = RecipeFactory()
        Recipe.objects.filter(pk=older.pk).update(published_at=older.published_at.replace(year=2020))

        assert list(RecipeSelector.search_published(ordering="bilinmeyen")) == [
            newer,
            older,
        ]

    def test_query_count_does_not_grow_with_result_count(self):
        def count_queries() -> int:
            with CaptureQueriesContext(connection) as context:
                for recipe in RecipeSelector.search_published():
                    _ = (recipe.province.name, recipe.category.name, recipe.author.username)
                    _ = list(recipe.recipe_images.all())
            return len(context)

        RecipeFactory()
        queries_for_one = count_queries()
        RecipeFactory.create_batch(4)

        assert count_queries() == queries_for_one


@pytest.mark.django_db
class TestRecipeSortBy:
    def test_most_viewed_orders_by_views_then_favorites(self):
        third = RecipeFactory(view_count=10, favorite_count=1)
        first = RecipeFactory(view_count=50, favorite_count=0)
        second = RecipeFactory(view_count=10, favorite_count=5)

        assert list(Recipe.objects.sort_by("most_viewed")) == [first, second, third]

    def test_favorites_orders_by_favorite_count(self):
        low = RecipeFactory(favorite_count=1)
        high = RecipeFactory(favorite_count=9)

        assert list(Recipe.objects.sort_by("favorites")) == [high, low]

    def test_popular_orders_by_favorites_then_views(self):
        fewer_views = RecipeFactory(favorite_count=5, view_count=1)
        more_views = RecipeFactory(favorite_count=5, view_count=9)

        assert list(Recipe.objects.sort_by("popular")) == [more_views, fewer_views]
