from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from recipes.models import Category  # noqa: F401


class CategoryQuerySet(models.QuerySet["Category"]):
    """Custom QuerySet for Category."""

    def active(self) -> CategoryQuerySet:
        """Return active categories."""
        return self.filter(
            is_active=True,
        )

    def inactive(self) -> CategoryQuerySet:
        """Return inactive categories."""
        return self.filter(
            is_active=False,
        )

    def sort_by_name(self) -> CategoryQuerySet:
        """Order categories alphabetically."""
        return self.order_by(
            "name",
        )

    def by_slug(
        self,
        slug: str,
    ) -> CategoryQuerySet:
        """Filter by slug."""
        return self.filter(
            slug=slug,
        )

    def search(
        self,
        query: str,
    ) -> CategoryQuerySet:
        """Search categories."""

        query = query.strip()

        if not query:
            return self

        return self.filter(
            name__icontains=query,
        )

    def with_recipe_count(self) -> CategoryQuerySet:
        """Annotate recipe count."""

        return self.annotate(
            recipe_count=models.Count(
                "recipes",
                distinct=True,
            ),
        )

    def has_recipes(self) -> CategoryQuerySet:
        """Return categories that contain recipes."""

        return (
            self.with_recipe_count()
            .filter(
                recipe_count__gt=0,
            )
        )

    def active_with_recipe_count(self) -> CategoryQuerySet:
        """Return active categories with recipe counts."""

        return (
            self.active()
            .with_recipe_count()
            .sort_by_name()
        )

    def active_with_recipes(self) -> CategoryQuerySet:
        """Return active categories containing recipes."""

        return (
            self.active()
            .has_recipes()
            .sort_by_name()
        )


class CategoryManager(models.Manager.from_queryset(CategoryQuerySet)):  # type: ignore[misc]
    """Custom manager for Category."""

    pass
