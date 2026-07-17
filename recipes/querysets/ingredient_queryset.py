from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from recipes.models import Ingredient  # noqa: F401


class IngredientQuerySet(models.QuerySet["Ingredient"]):
    """Custom QuerySet for Ingredient."""

    def active(self) -> IngredientQuerySet:
        """Return active ingredients."""
        return self.filter(
            is_active=True,
        )

    def inactive(self) -> IngredientQuerySet:
        """Return inactive ingredients."""
        return self.filter(
            is_active=False,
        )

    def sort_by_name(self) -> IngredientQuerySet:
        """Order ingredients alphabetically."""
        return self.order_by(
            "name",
        )

    def by_slug(
        self,
        slug: str,
    ) -> IngredientQuerySet:
        """Filter by slug."""
        return self.filter(
            slug=slug,
        )

    def search(
        self,
        query: str,
    ) -> IngredientQuerySet:
        """Search ingredients."""

        query = query.strip()

        if not query:
            return self

        return self.filter(
            name__icontains=query,
        )

    def with_recipe_count(self) -> IngredientQuerySet:
        """Annotate recipe count."""

        return self.annotate(
            recipe_count=models.Count(
                "recipe_ingredients",
                distinct=True,
            ),
        )

    def has_recipes(self) -> IngredientQuerySet:
        """Return ingredients used by at least one recipe."""

        return (
            self.with_recipe_count()
            .filter(
                recipe_count__gt=0,
            )
        )

    def active_with_recipe_count(self) -> IngredientQuerySet:
        """Return active ingredients with recipe counts."""

        return (
            self.active()
            .with_recipe_count()
            .sort_by_name()
        )

    def active_with_recipes(self) -> IngredientQuerySet:
        """Return active ingredients that have recipes."""

        return (
            self.active()
            .has_recipes()
            .sort_by_name()
        )


class IngredientManager(models.Manager.from_queryset(IngredientQuerySet)):  # type: ignore[misc]
    """Custom manager for Ingredient."""

    pass
