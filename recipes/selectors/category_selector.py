from __future__ import annotations

from django.db.models import QuerySet

from recipes.models import Category


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
