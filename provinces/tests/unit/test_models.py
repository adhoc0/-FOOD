"""Province ve Region model testleri."""

import pytest
from django.db import IntegrityError, transaction

from provinces.models import Province, Region
from tests.factories import ProvinceFactory, RegionFactory


@pytest.mark.django_db
class TestRegionModel:
    def test_str_returns_name(self):
        assert str(RegionFactory(name="Ege")) == "Ege"

    def test_default_map_color_is_valid_hex(self):
        region = RegionFactory()

        assert region.map_color == "#2E7D32"

    def test_default_ordering_uses_display_order_then_name(self):
        second = RegionFactory(name="Akdeniz", slug="akdeniz", display_order=2)
        first_b = RegionFactory(name="Marmara", slug="marmara", display_order=1)
        first_a = RegionFactory(name="Karadeniz", slug="karadeniz", display_order=1)

        assert list(Region.objects.all()) == [first_a, first_b, second]

    def test_name_must_be_unique(self):
        RegionFactory(name="Ege", slug="ege")

        with pytest.raises(IntegrityError), transaction.atomic():
            RegionFactory(name="Ege", slug="ege-2")


@pytest.mark.django_db
class TestProvinceModel:
    def test_str_pads_plate_code(self):
        province = ProvinceFactory(plate_code=7, name="Antalya")

        assert str(province) == "07 - Antalya"

    def test_get_absolute_url_uses_slug(self):
        province = ProvinceFactory(slug="gaziantep")

        assert province.get_absolute_url() == "/il/gaziantep/"

    def test_default_ordering_is_plate_code(self):
        late = ProvinceFactory(plate_code=60, slug="il-60")
        early = ProvinceFactory(plate_code=6, slug="il-6")

        assert list(Province.objects.all()) == [early, late]

    def test_plate_code_must_be_unique(self):
        ProvinceFactory(plate_code=27, slug="gaziantep")

        with pytest.raises(IntegrityError), transaction.atomic():
            ProvinceFactory(plate_code=27, slug="baska-slug")

    def test_region_cannot_be_deleted_while_provinces_exist(self):
        province = ProvinceFactory()

        with pytest.raises(Exception, match="protected|PROTECT|Protected"):
            province.region.delete()
