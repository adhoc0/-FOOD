from __future__ import annotations

from django.db.models import QuerySet

from recipes.models import Category, Recipe


class CategorySelector:
    """Kategori verisini yalnızca okuyan sorgular."""

    @staticmethod
    def get_all_active() -> QuerySet[Category]:
        return Category.objects.active().sort_by_name()

    @staticmethod
    def get_by_slug(slug: str) -> Category | None:
        return Category.objects.active().by_slug(slug).first()

    @staticmethod
    def get_with_recipe_count() -> QuerySet[Category]:
        return Category.objects.active_with_recipe_count()

    @staticmethod
    def get_published_recipes(slug: str) -> tuple[Category | None, QuerySet[Recipe]]:
        """Aktif kategori ile o kategoriye ait yayınlanmış tarifleri okur."""
        category = CategorySelector.get_by_slug(slug)
        if category is None:
            return None, Recipe.objects.none()
        recipes = Recipe.objects.published_with_related().by_category(category).recent()
        return category, recipes
