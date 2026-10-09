from __future__ import annotations

from django.db.models import QuerySet

from recipes.choices import Status
from recipes.models import Recipe
from recipes.selectors import RecipeSelector


class SearchService:
    """Service layer responsible for search operations."""

    @staticmethod
    def search_recipes(
        query: str,
        limit: int | None = None,
    ) -> QuerySet[Recipe]:
        """Search published recipes, most viewed first."""

        queryset = RecipeSelector.search_published(
            query=query,
            ordering="most_viewed",
        )

        if limit is not None:
            return queryset[:limit]

        return queryset

    @staticmethod
    def get_search_suggestions(
        query: str,
        limit: int = 5,
    ) -> QuerySet:
        """Return recipe title suggestions."""

        cleaned_query = query.strip()

        if len(cleaned_query) < 2:
            return Recipe.objects.none()

        return (
            Recipe.objects.filter(
                is_active=True,
                status=Status.PUBLISHED,
                title__icontains=cleaned_query,
            )
            .values_list(
                "title",
                "slug",
            )
            .order_by(
                "-view_count",
            )[:limit]
        )
