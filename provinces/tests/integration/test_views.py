"""Province view entegrasyon testleri."""

import pytest
from django.test import Client
from django.urls import reverse

from tests.factories import (
    DraftRecipeFactory,
    ProvinceFactory,
    RecipeFactory,
    RegionFactory,
)


@pytest.mark.django_db
class TestProvinceListView:
    def test_renders_active_provinces_only(self):
        active = ProvinceFactory(name="Gaziantep", slug="gaziantep")
        ProvinceFactory(name="Pasif", slug="pasif", is_active=False)

        response = Client().get(reverse("provinces:list"))

        assert response.status_code == 200
        assert list(response.context["provinces"]) == [active]

    def test_uses_expected_template(self):
        response = Client().get(reverse("provinces:list"))

        assert "provinces/list.html" in [t.name for t in response.templates]

    def test_filters_by_region_query_parameter(self):
        region = RegionFactory(slug="ege", name="Ege")
        in_region = ProvinceFactory(region=region)
        ProvinceFactory()

        response = Client().get(reverse("provinces:list"), {"region": "ege"})

        assert list(response.context["provinces"]) == [in_region]
        assert response.context["current_region"] == "ege"

    def test_exposes_active_regions_for_filter_menu(self):
        active = RegionFactory(name="Ege", slug="ege")
        RegionFactory(name="Pasif", slug="pasif", is_active=False)

        response = Client().get(reverse("provinces:list"))

        assert list(response.context["regions"]) == [active]


@pytest.mark.django_db
class TestProvinceDetailView:
    def test_renders_active_province(self):
        province = ProvinceFactory(name="Konya", slug="konya")

        response = Client().get(province.get_absolute_url())

        assert response.status_code == 200
        assert response.context["province"] == province
        assert "Konya" in response.content.decode()

    def test_returns_404_for_inactive_province(self):
        province = ProvinceFactory(slug="pasif", is_active=False)

        assert Client().get(province.get_absolute_url()).status_code == 404

    def test_returns_404_for_unknown_slug(self):
        response = Client().get(reverse("provinces:detail", kwargs={"slug": "yok"}))

        assert response.status_code == 404

    def test_lists_only_published_recipes_of_the_province(self):
        province = ProvinceFactory()
        published = RecipeFactory(province=province, title="Yayındaki Tarif")
        draft = DraftRecipeFactory(province=province, title="Taslak Tarif")
        other = RecipeFactory(title="Başka İl Tarifi")

        response = Client().get(province.get_absolute_url())

        assert list(response.context["recipes"]) == [published]
        content = response.content.decode()
        assert draft.title not in content
        assert other.title not in content

    def test_limits_featured_recipes(self):
        province = ProvinceFactory()
        RecipeFactory.create_batch(8, province=province)

        response = Client().get(province.get_absolute_url())

        assert len(response.context["recipes"]) == 6
