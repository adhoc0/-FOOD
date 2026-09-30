"""Province ve Region servis testleri."""

import pytest

from provinces.services import (
    activate_region,
    create_region,
    deactivate_region,
    update_region,
)
from provinces.services.province_service import (
    activate_province,
    deactivate_province,
    feature_province,
    unfeature_province,
)
from tests.factories import ProvinceFactory, RegionFactory


@pytest.mark.django_db
class TestProvinceService:
    def test_deactivate_and_activate_persist_flag(self):
        province = ProvinceFactory(is_active=True)

        deactivate_province(province)
        province.refresh_from_db()
        assert province.is_active is False

        activate_province(province)
        province.refresh_from_db()
        assert province.is_active is True

    def test_feature_and_unfeature_persist_flag(self):
        province = ProvinceFactory(is_featured=False)

        feature_province(province)
        province.refresh_from_db()
        assert province.is_featured is True

        unfeature_province(province)
        province.refresh_from_db()
        assert province.is_featured is False

    def test_status_changes_only_touch_their_own_fields(self):
        province = ProvinceFactory(is_active=True, is_featured=True)

        deactivate_province(province)
        province.refresh_from_db()

        assert province.is_featured is True


@pytest.mark.django_db
class TestRegionService:
    def test_create_region_persists_data(self):
        region = create_region(name="Ege", slug="ege", display_order=3)

        region.refresh_from_db()
        assert (region.name, region.slug, region.display_order) == ("Ege", "ege", 3)

    def test_update_region_changes_given_fields_only(self):
        region = RegionFactory(name="Eski", slug="eski", display_order=5)

        update_region(region, name="Yeni")

        region.refresh_from_db()
        assert region.name == "Yeni"
        assert region.display_order == 5

    def test_deactivate_and_activate_region(self):
        region = RegionFactory(is_active=True)

        deactivate_region(region)
        region.refresh_from_db()
        assert region.is_active is False

        activate_region(region)
        region.refresh_from_db()
        assert region.is_active is True
