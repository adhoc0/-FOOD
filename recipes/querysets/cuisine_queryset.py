from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from recipes.models.cuisine import Cuisine  # noqa: F401


class CuisineQuerySet(models.QuerySet["Cuisine"]):
    """Custom QuerySet for Cuisine."""

    def active(self) -> CuisineQuerySet:
        """Return active cuisines."""
        return self.filter(
            is_active=True,
        )

    def inactive(self) -> CuisineQuerySet:
        """Return inactive cuisines."""
        return self.filter(
            is_active=False,
        )

    def sort_by_name(self) -> CuisineQuerySet:
        """Order cuisines alphabetically."""
        return self.order_by(
            "name",
        )

    def by_slug(
        self,
        slug: str,
    ) -> CuisineQuerySet:
        """Filter by slug."""
        return self.filter(
            slug=slug,
        )

    def search(
        self,
        query: str,
    ) -> CuisineQuerySet:
        """Search cuisines."""

        query = query.strip()

        if not query:
            return self

        return self.filter(
            name__icontains=query,
        )


class CuisineManager(models.Manager.from_queryset(CuisineQuerySet)):  # type: ignore[misc]
    """Custom manager for Cuisine."""

    pass
