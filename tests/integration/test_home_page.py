"""Ana sayfa entegrasyon testleri."""

import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import CategoryFactory, RecipeFactory


@pytest.mark.django_db
class TestHomePageView:
    """Ana sayfanın servis katmanındaki context verisini kullanmasını doğrular."""

    def test_context_contains_homepage_service_data(self):
        recipe = RecipeFactory(is_featured=True)

        response = Client().get(reverse("pages:home"))

        assert response.status_code == 200
        assert recipe in response.context["featured_recipes"]
        assert recipe in response.context["latest_recipes"]
        assert recipe.province in response.context["popular_provinces"]
        assert response.context["total_recipes"] == 1
        assert response.context["total_categories"] == 1
        assert response.context["total_provinces"] == 1
        assert response.context["total_users"] == 1

    def test_unicode_category_slug_is_rendered_and_resolved(self):
        category = CategoryFactory(slug="çorba")
        category_url = reverse(
            "recipes:category_detail",
            kwargs={"slug": category.slug},
        )

        response = Client().get(reverse("pages:home"))

        assert response.status_code == 200
        assert category_url.encode() in response.content
        assert Client().get(category_url).status_code == 200

    def test_map_markup_is_rendered_on_homepage(self):
        response = Client().get(reverse("pages:home"))

        assert response.status_code == 200
        assert b"turkey-map__land" in response.content
