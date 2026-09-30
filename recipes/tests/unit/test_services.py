"""SearchService ve CategoryService testleri."""

import pytest

from recipes.models import Category
from recipes.services import CategoryService, SearchService
from tests.factories import CategoryFactory, DraftRecipeFactory, RecipeFactory


@pytest.mark.django_db
class TestSearchService:
    def test_matches_title_case_insensitively(self):
        match = RecipeFactory(title="Ali Nazik Kebabı")
        RecipeFactory(title="Mantı")

        assert list(SearchService.search_recipes("ali nazik")) == [match]

    def test_blank_query_returns_all_published_recipes(self):
        RecipeFactory.create_batch(2)

        assert SearchService.search_recipes("   ").count() == 2

    def test_excludes_drafts_and_inactive_recipes(self):
        published = RecipeFactory(title="Yayinda Corba")
        DraftRecipeFactory(title="Taslak Corba")
        RecipeFactory(title="Pasif Corba", is_active=False)

        assert list(SearchService.search_recipes("corba")) == [published]

    def test_orders_by_view_count_then_favorite_count(self):
        popular = RecipeFactory(title="Kebap A", view_count=50)
        favorite = RecipeFactory(title="Kebap B", view_count=10, favorite_count=9)
        quiet = RecipeFactory(title="Kebap C", view_count=10, favorite_count=1)

        assert list(SearchService.search_recipes("kebap")) == [popular, favorite, quiet]

    def test_limit_truncates_results(self):
        RecipeFactory.create_batch(3, title="Pilav")

        assert len(SearchService.search_recipes("pilav", limit=2)) == 2

    def test_suggestions_require_at_least_two_characters(self):
        RecipeFactory(title="Pilav")

        assert list(SearchService.get_search_suggestions("p")) == []
        assert list(SearchService.get_search_suggestions(" ")) == []

    def test_suggestions_return_title_and_slug_pairs(self):
        recipe = RecipeFactory(title="Pilav Üstü Kavurma")
        DraftRecipeFactory(title="Pilav Taslağı")

        assert list(SearchService.get_search_suggestions("pilav")) == [
            (recipe.title, recipe.slug),
        ]

    def test_suggestions_respect_limit(self):
        RecipeFactory.create_batch(4, title="Sarma")

        assert len(SearchService.get_search_suggestions("sarma", limit=3)) == 3


@pytest.mark.django_db
class TestCategoryService:
    def test_create_persists_category(self):
        category = CategoryService.create(name="Çorbalar", slug="corbalar")

        assert Category.objects.get(pk=category.pk).name == "Çorbalar"

    def test_update_changes_only_given_fields(self):
        category = CategoryFactory(name="Eski", slug="eski", description="Açıklama")

        CategoryService.update(category, name="Yeni")

        category.refresh_from_db()
        assert category.name == "Yeni"
        assert category.description == "Açıklama"

    def test_update_without_data_is_a_no_op(self):
        category = CategoryFactory()

        assert CategoryService.update(category) is category

    def test_deactivate_and_activate(self):
        category = CategoryFactory(is_active=True)

        CategoryService.deactivate(category)
        category.refresh_from_db()
        assert category.is_active is False

        CategoryService.activate(category)
        category.refresh_from_db()
        assert category.is_active is True

    def test_delete_removes_category(self):
        category = CategoryFactory()

        CategoryService.delete(category)

        assert not Category.objects.filter(pk=category.pk).exists()
