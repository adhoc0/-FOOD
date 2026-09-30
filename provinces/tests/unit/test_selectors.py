"""Province ve Region selector testleri."""

import pytest

from provinces.selectors import ProvinceSelector, RegionSelector
from tests.factories import ProvinceFactory, RegionFactory


@pytest.mark.django_db
class TestProvinceSelector:
    def test_get_active_list_excludes_inactive_and_orders_by_plate_code(self):
        late = ProvinceFactory(plate_code=60, slug="il-60")
        early = ProvinceFactory(plate_code=6, slug="il-6")
        ProvinceFactory(is_active=False)

        assert list(ProvinceSelector.get_active_list()) == [early, late]

    def test_get_active_list_filters_by_region_slug(self):
        region = RegionFactory(slug="ege", name="Ege")
        in_region = ProvinceFactory(region=region)
        ProvinceFactory()

        result = ProvinceSelector.get_active_list(region_slug="ege")

        assert list(result) == [in_region]

    def test_get_active_list_loads_region_without_extra_queries(
        self, django_assert_num_queries
    ):
        ProvinceFactory.create_batch(3)

        with django_assert_num_queries(1):
            for province in ProvinceSelector.get_active_list():
                _ = province.region.name

    def test_get_active_by_slug_returns_active_province(self):
        province = ProvinceFactory(slug="konya")

        assert ProvinceSelector.get_active_by_slug("konya") == province

    def test_get_active_by_slug_ignores_inactive_and_unknown(self):
        ProvinceFactory(slug="pasif", is_active=False)

        assert ProvinceSelector.get_active_by_slug("pasif") is None
        assert ProvinceSelector.get_active_by_slug("yok") is None

    def test_get_map_entries_lists_only_active_provinces_in_plate_order(self):
        second = ProvinceFactory(plate_code=2, name="Adıyaman", slug="adiyaman")
        first = ProvinceFactory(plate_code=1, name="Adana", slug="adana")
        ProvinceFactory(plate_code=3, is_active=False)

        assert ProvinceSelector.get_map_entries() == [
            {"plate_code": 1, "name": "Adana", "url": first.get_absolute_url()},
            {"plate_code": 2, "name": "Adıyaman", "url": second.get_absolute_url()},
        ]


@pytest.mark.django_db
class TestRegionSelector:
    def test_get_active_list_orders_by_display_order_then_name(self):
        later = RegionFactory(name="Akdeniz", slug="akdeniz", display_order=2)
        first = RegionFactory(name="Marmara", slug="marmara", display_order=1)
        RegionFactory(is_active=False)

        assert list(RegionSelector.get_active_list()) == [first, later]
