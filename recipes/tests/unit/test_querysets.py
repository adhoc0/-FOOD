"""CategoryQuerySet testleri."""

import pytest

from recipes.models import Category
from tests.factories import CategoryFactory, RecipeFactory


@pytest.mark.django_db
class TestCategoryQuerySet:
    def test_active_and_inactive_are_complements(self):
        active = CategoryFactory(is_active=True)
        inactive = CategoryFactory(is_active=False)

        assert list(Category.objects.active()) == [active]
        assert list(Category.objects.inactive()) == [inactive]

    def test_sort_by_name_orders_alphabetically(self):
        zeytinyagli = CategoryFactory(name="Zeytinyağlılar", slug="zeytinyaglilar")
        corbalar = CategoryFactory(name="Çorbalar", slug="corbalar")
        ana_yemek = CategoryFactory(name="Ana Yemekler", slug="ana-yemekler")

        ordered = list(Category.objects.sort_by_name())

        assert ordered[0] == ana_yemek
        assert set(ordered) == {ana_yemek, corbalar, zeytinyagli}

    def test_by_slug_filters_single_category(self):
        category = CategoryFactory(slug="tatlilar")
        CategoryFactory()

        assert list(Category.objects.by_slug("tatlilar")) == [category]

    def test_recipe_count_counts_recipes_once(self):
        category = CategoryFactory()
        RecipeFactory.create_batch(3, category=category)

        annotated = Category.objects.with_recipe_count().get(pk=category.pk)

        assert annotated.recipe_count == 3

    def test_has_recipes_excludes_empty_categories(self):
        used = CategoryFactory()
        RecipeFactory(category=used)
        CategoryFactory()

        assert list(Category.objects.has_recipes()) == [used]

    def test_active_with_recipes_excludes_inactive_categories(self):
        active = CategoryFactory()
        RecipeFactory(category=active)
        inactive = CategoryFactory(is_active=False)
        RecipeFactory(category=inactive)

        assert list(Category.objects.active_with_recipes()) == [active]
