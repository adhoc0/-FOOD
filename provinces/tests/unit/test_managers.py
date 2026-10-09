"""Province manager ve queryset testleri."""

import pytest

from provinces.models import Province
from provinces.querysets.province_queryset import ProvinceQuerySet
from tests.factories import ProvinceFactory, RecipeFactory, RegionFactory


@pytest.mark.django_db
class TestProvinceQuerySet:
    def test_manager_returns_province_queryset(self):
        assert isinstance(Province.objects.all(), ProvinceQuerySet)

    def test_active_and_inactive_are_complements(self):
        active = ProvinceFactory(is_active=True)
        inactive = ProvinceFactory(is_active=False)

        assert list(Province.objects.active()) == [active]
        assert list(Province.objects.inactive()) == [inactive]

    def test_featured_returns_only_featured(self):
        featured = ProvinceFactory(is_featured=True)
        ProvinceFactory(is_featured=False)

        assert list(Province.objects.featured()) == [featured]

    def test_ordered_by_code_and_sort_by_name(self):
        zonguldak = ProvinceFactory(plate_code=67, name="Zonguldak", slug="zonguldak")
        adana = ProvinceFactory(plate_code=90, name="Adana", slug="adana")

        assert list(Province.objects.ordered_by_code()) == [zonguldak, adana]
        assert list(Province.objects.sort_by_name()) == [adana, zonguldak]

    def test_by_slug_by_plate_code_and_by_region(self):
        province = ProvinceFactory(slug="konya", plate_code=42)
        ProvinceFactory()

        assert list(Province.objects.by_slug("konya")) == [province]
        assert list(Province.objects.by_plate_code(42)) == [province]
        assert list(Province.objects.by_region(province.region)) == [province]

    def test_search_matches_name_and_slug_case_insensitively(self):
        province = ProvinceFactory(name="Gaziantep", slug="gaziantep")
        ProvinceFactory(name="Konya", slug="konya")

        assert list(Province.objects.search("gazi")) == [province]
        assert list(Province.objects.search("  GAZIANTEP ")) == [province]

    def test_search_with_blank_query_returns_everything(self):
        ProvinceFactory()
        ProvinceFactory()

        assert Province.objects.search("   ").count() == 2

    def test_with_related_avoids_region_query(self, django_assert_num_queries):
        ProvinceFactory()

        with django_assert_num_queries(1):
            province = Province.objects.with_related().get()
            _ = province.region.name

    def test_recipe_count_counts_each_recipe_once(self):
        province = ProvinceFactory()
        RecipeFactory.create_batch(2, province=province)
        ProvinceFactory()

        annotated = Province.objects.with_recipe_count().get(pk=province.pk)

        assert annotated.recipe_count == 2

    def test_has_recipes_excludes_empty_provinces(self):
        with_recipe = ProvinceFactory()
        RecipeFactory(province=with_recipe)
        ProvinceFactory()

        assert list(Province.objects.has_recipes()) == [with_recipe]

    def test_active_with_recipes_excludes_inactive_and_empty(self):
        active = ProvinceFactory(name="Aydın", slug="aydin")
        RecipeFactory(province=active)
        inactive = ProvinceFactory(is_active=False)
        RecipeFactory(province=inactive)
        ProvinceFactory(name="Boş", slug="bos")

        assert list(Province.objects.active_with_recipes()) == [active]

    def test_active_with_recipe_count_is_sorted_by_name(self):
        zara = ProvinceFactory(name="Zara", slug="zara")
        adana = ProvinceFactory(name="Adana", slug="adana")

        assert list(Province.objects.active_with_recipe_count()) == [adana, zara]

    def test_region_fixture_is_reusable_across_provinces(self):
        region = RegionFactory()
        ProvinceFactory.create_batch(2, region=region)

        assert Province.objects.by_region(region).count() == 2
