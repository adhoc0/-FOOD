"""Province URL ve sitemap testleri."""

import pytest
from django.urls import resolve, reverse

from provinces.sitemaps import ProvinceSitemap
from provinces.views import ProvinceDetailView, ProvinceListView
from tests.factories import ProvinceFactory


def test_list_url_is_stable():
    assert reverse("provinces:list") == "/il/"
    assert resolve("/il/").func.view_class is ProvinceListView


def test_detail_url_is_built_from_slug():
    url = reverse("provinces:detail", kwargs={"slug": "gaziantep"})

    assert url == "/il/gaziantep/"
    assert resolve(url).func.view_class is ProvinceDetailView


@pytest.mark.django_db
def test_sitemap_contains_only_active_provinces():
    active = ProvinceFactory(slug="aktif")
    ProvinceFactory(slug="pasif", is_active=False)

    sitemap = ProvinceSitemap()

    assert list(sitemap.items()) == [active]
    assert sitemap.location(active) == "/il/aktif/"
    assert sitemap.lastmod(active) == active.updated_at
