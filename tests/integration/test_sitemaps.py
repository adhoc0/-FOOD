"""sitemap.xml içeriği testleri."""

import pytest
from django.urls import reverse

from tests.factories import DraftRecipeFactory, ProvinceFactory, RecipeFactory


@pytest.mark.django_db
class TestSitemap:
    def _get(self, client):
        response = client.get("/sitemap.xml")
        assert response.status_code == 200
        return response.content.decode()

    def test_contains_all_static_pages(self, client):
        body = self._get(client)

        for name in (
            "pages:home",
            "pages:about",
            "pages:contact",
            "pages:privacy",
            "pages:cookies",
            "pages:kvkk",
            "pages:terms",
        ):
            assert reverse(name) in body

    def test_contains_published_recipe_and_province(self, client):
        recipe = RecipeFactory()
        province = ProvinceFactory()

        body = self._get(client)

        assert recipe.get_absolute_url() in body
        assert province.get_absolute_url() in body

    def test_excludes_draft_and_inactive_recipes(self, client):
        draft = DraftRecipeFactory()
        inactive = RecipeFactory(is_active=False)

        body = self._get(client)

        assert draft.get_absolute_url() not in body
        assert inactive.get_absolute_url() not in body
