"""Tarif liste ve detay sayfası testleri."""

import pytest
from django.core.cache import cache
from django.test import Client
from django.urls import reverse

from tests.factories import (
    CategoryFactory,
    DraftRecipeFactory,
    ProvinceFactory,
    RecipeFactory,
)


@pytest.fixture(autouse=True)
def _clear_cache():
    cache.clear()
    yield
    cache.clear()


@pytest.mark.django_db
class TestRecipeListView:
    def test_lists_only_published_recipes(self, client):
        published = RecipeFactory(title="Yayında Tarif")
        DraftRecipeFactory(title="Taslak Tarif")

        response = client.get(reverse("recipes:list"))

        assert response.status_code == 200
        assert list(response.context["recipes"]) == [published]

    def test_filters_by_province_and_category(self, client):
        province = ProvinceFactory()
        category = CategoryFactory()
        match = RecipeFactory(province=province, category=category)
        RecipeFactory()

        response = client.get(
            reverse("recipes:list"),
            {"province": province.slug, "category": category.slug},
        )

        assert list(response.context["recipes"]) == [match]
        assert response.context["current_province"] == province.slug


@pytest.mark.django_db
class TestRecipeDetailView:
    def test_renders_published_recipe(self, client):
        recipe = RecipeFactory(title="Ali Nazik")

        response = client.get(recipe.get_absolute_url())

        assert response.status_code == 200
        assert "Ali Nazik" in response.content.decode()

    def test_increments_view_count(self, client):
        recipe = RecipeFactory()

        client.get(recipe.get_absolute_url())
        recipe.refresh_from_db()

        assert recipe.view_count == 1

    def test_draft_recipe_returns_404(self, client):
        recipe = DraftRecipeFactory()

        assert client.get(recipe.get_absolute_url()).status_code == 404

    def test_unknown_slug_returns_404(self, client):
        response = client.get(reverse("recipes:recipe_detail", args=["yok"]))

        assert response.status_code == 404

    def test_meta_fallbacks(self, client):
        recipe = RecipeFactory(meta_title="", meta_description="")

        response = client.get(recipe.get_absolute_url())

        assert recipe.title in response.context["meta_title"]
        assert response.context["meta_description"] == recipe.summary[:160]

    def test_repeated_visits_by_same_visitor_count_once(self, client):
        recipe = RecipeFactory()

        for _ in range(3):
            client.get(recipe.get_absolute_url())

        recipe.refresh_from_db()
        assert recipe.view_count == 1

    def test_different_visitors_are_counted_separately(self):
        recipe = RecipeFactory()

        Client(REMOTE_ADDR="10.1.0.1").get(recipe.get_absolute_url())
        Client(REMOTE_ADDR="10.1.0.2").get(recipe.get_absolute_url())

        recipe.refresh_from_db()
        assert recipe.view_count == 2

    def test_head_requests_are_not_counted(self, client):
        recipe = RecipeFactory()

        client.head(recipe.get_absolute_url())

        recipe.refresh_from_db()
        assert recipe.view_count == 0

    def test_counts_again_after_window_expires(self, client):
        recipe = RecipeFactory()

        client.get(recipe.get_absolute_url())
        cache.clear()  # dedupe penceresi doldu varsayımı
        client.get(recipe.get_absolute_url())

        recipe.refresh_from_db()
        assert recipe.view_count == 2
