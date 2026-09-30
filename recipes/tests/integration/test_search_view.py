"""SearchView entegrasyon testleri."""

import pytest
from django.test import Client
from django.urls import reverse

from recipes.choices import Difficulty
from tests.factories import CategoryFactory, DraftRecipeFactory, ProvinceFactory, RecipeFactory

SEARCH_URL = "recipes:search"


@pytest.mark.django_db
class TestSearchView:
    def test_total_results_matches_filtered_count(self):
        RecipeFactory(title="Pilav A")
        RecipeFactory(title="Pilav B")
        RecipeFactory(title="Mantı")

        response = Client().get(reverse(SEARCH_URL), {"q": "pilav"})

        assert response.context["total_results"] == 2

    def test_drafts_are_not_listed(self):
        published = RecipeFactory(title="Kebap A")
        DraftRecipeFactory(title="Kebap B")

        response = Client().get(reverse(SEARCH_URL), {"q": "kebap"})

        assert list(response.context["recipes"]) == [published]

    def test_filters_are_combined(self):
        province = ProvinceFactory()
        category = CategoryFactory()
        match = RecipeFactory(
            title="Corba A",
            province=province,
            category=category,
            difficulty=Difficulty.EASY,
        )
        RecipeFactory(title="Corba B", province=province, difficulty=Difficulty.EASY)

        response = Client().get(
            reverse(SEARCH_URL),
            {
                "q": "corba",
                "province": province.slug,
                "category": category.slug,
                "difficulty": Difficulty.EASY,
            },
        )

        assert list(response.context["recipes"]) == [match]
        assert response.context["current_province"] == province.slug
        assert response.context["current_category"] == category.slug
        assert response.context["current_difficulty"] == Difficulty.EASY

    def test_sort_parameter_changes_order(self):
        popular = RecipeFactory(title="Sarma A", favorite_count=9)
        quiet = RecipeFactory(title="Sarma B", favorite_count=1)

        response = Client().get(reverse(SEARCH_URL), {"q": "sarma", "sort": "favorites"})

        assert list(response.context["recipes"]) == [popular, quiet]
        assert response.context["current_sort"] == "favorites"

    def test_unknown_sort_does_not_break_the_page(self):
        RecipeFactory(title="Pide")

        response = Client().get(reverse(SEARCH_URL), {"q": "pide", "sort": "xyz"})

        assert response.status_code == 200
        assert response.context["total_results"] == 1

    def test_meta_title_reflects_query(self):
        response = Client().get(reverse(SEARCH_URL), {"q": "mantı"})

        assert "mantı" in response.context["meta_title"]

    def test_query_count_is_independent_of_result_count(self, django_assert_max_num_queries):
        RecipeFactory.create_batch(6, title="Lahmacun")

        with django_assert_max_num_queries(12):
            response = Client().get(reverse(SEARCH_URL), {"q": "lahmacun"})

        assert response.status_code == 200
