from __future__ import annotations

from django.db.models import QuerySet

from provinces.models import Province
from recipes.models import Category, Recipe


class RecipeSelector:
    """Tarif verisini yalnızca okuyan sorgular."""

    @staticmethod
    def get_published_list() -> QuerySet[Recipe]:
        return Recipe.objects.published_with_related().recent()

    @staticmethod
    def get_filtered_published_list(
        *,
        province_slug: str = "",
        category_slug: str = "",
    ) -> QuerySet[Recipe]:
        """Yayındaki tarifleri filtreleriyle birlikte okur."""
        queryset = Recipe.objects.published_with_related().recent()
        if province_slug:
            queryset = queryset.by_province_slug(province_slug)
        if category_slug:
            queryset = queryset.by_category_slug(category_slug)
        return queryset

    @staticmethod
    def get_recipe_detail(slug: str) -> Recipe | None:
        return Recipe.objects.published_with_related().by_slug(slug).first()

    @staticmethod
    def get_featured() -> QuerySet[Recipe]:
        return Recipe.objects.featured().with_related().recent()

    @staticmethod
    def get_by_province(province: Province) -> QuerySet[Recipe]:
        return Recipe.objects.published_with_related().by_province(province).recent()

    @staticmethod
    def get_by_category(category: Category) -> QuerySet[Recipe]:
        return Recipe.objects.published_with_related().by_category(category).recent()

    @staticmethod
    def get_related_recipes(recipe: Recipe) -> QuerySet[Recipe]:
        return Recipe.objects.related(recipe)

    @staticmethod
    def get_published_count() -> int:
        return Recipe.objects.published().count()
