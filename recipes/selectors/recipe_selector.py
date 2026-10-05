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
    def search_published(
        *,
        query: str = "",
        province_slug: str = "",
        category_slug: str = "",
        difficulty: str = "",
        ordering: str = "latest",
    ) -> QuerySet[Recipe]:
        """Yayındaki tarifleri başlığa göre arar, süzer ve sıralar."""
        queryset = Recipe.objects.published_with_related()

        cleaned_query = query.strip()
        if cleaned_query:
            queryset = queryset.filter(title__icontains=cleaned_query)
        if province_slug:
            queryset = queryset.by_province_slug(province_slug)
        if category_slug:
            queryset = queryset.by_category_slug(category_slug)
        if difficulty:
            queryset = queryset.by_difficulty(difficulty)

        return queryset.sort_by(ordering)

    @staticmethod
    def get_recipe_detail(slug: str) -> Recipe | None:
        return Recipe.objects.by_slug(slug).first()

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
