from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from recipes.models.tag import Tag  # noqa: F401


class TagQuerySet(models.QuerySet["Tag"]):
    """Custom QuerySet for Tag."""

    def active(self) -> TagQuerySet:
        """Return active tags."""
        return self.filter(
            is_active=True,
        )

    def inactive(self) -> TagQuerySet:
        """Return inactive tags."""
        return self.filter(
            is_active=False,
        )

    def sort_by_name(self) -> TagQuerySet:
        """Order tags alphabetically."""
        return self.order_by(
            "name",
        )

    def by_slug(
        self,
        slug: str,
    ) -> TagQuerySet:
        """Filter by slug."""
        return self.filter(
            slug=slug,
        )

    def search(
        self,
        query: str,
    ) -> TagQuerySet:
        """Search tags by name."""

        query = query.strip()

        if not query:
            return self

        return self.filter(
            name__icontains=query,
        )

    def with_recipe_count(self) -> TagQuerySet:
        """Annotate recipe count."""

        return self.annotate(
            recipe_count=models.Count(
                "recipe_tags",
                distinct=True,
            ),
        )

    def has_recipes(self) -> TagQuerySet:
        """Return tags assigned to at least one recipe."""

        return (
            self.with_recipe_count()
            .filter(
                recipe_count__gt=0,
            )
        )

    def active_with_recipe_count(self) -> TagQuerySet:
        """Return active tags with recipe counts."""

        return (
            self.active()
            .with_recipe_count()
            .sort_by_name()
        )

    def active_with_recipes(self) -> TagQuerySet:
        """Return active tags that have recipes."""

        return (
            self.active()
            .has_recipes()
            .sort_by_name()
        )


class TagManager(models.Manager.from_queryset(TagQuerySet)):  # type: ignore[misc]
    """Custom manager for Tag."""

    pass
