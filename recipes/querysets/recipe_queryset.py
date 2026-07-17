from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models
from django.db.models import Q

from recipes.choices import Status

if TYPE_CHECKING:
    from provinces.models import Province
    from recipes.models.category import Category
    from recipes.models.recipe import Recipe


class RecipeQuerySet(models.QuerySet["Recipe"]):
    """Custom QuerySet for Recipe."""

    def active(self) -> RecipeQuerySet:
        """Return active recipes."""
        return self.filter(
            is_active=True,
        )

    def inactive(self) -> RecipeQuerySet:
        """Return inactive recipes."""
        return self.filter(
            is_active=False,
        )

    def published(self) -> RecipeQuerySet:
        """Return published recipes."""
        return self.active().filter(
            status=Status.PUBLISHED,
        )

    def featured(self) -> RecipeQuerySet:
        """Return featured recipes."""
        return self.published().filter(
            is_featured=True,
        )

    def recent(self) -> RecipeQuerySet:
        """Return newest published recipes."""
        return self.published().sort_by(
            "latest",
        )

    def popular(self) -> RecipeQuerySet:
        """Return most popular recipes."""
        return self.published().sort_by(
            "popular",
        )

    def with_related(self) -> RecipeQuerySet:
        """Load related objects."""

        return (
            self.select_related(
                "province",
                "category",
                "author",
            )
            .prefetch_related(
                "recipe_images",
                "recipe_ingredients",
                "recipe_tags",
            )
        )

    def published_with_related(self) -> RecipeQuerySet:
        """Return published recipes with related objects."""

        return (
            self.published()
            .with_related()
        )

    def by_slug(
        self,
        slug: str,
    ) -> RecipeQuerySet:
        """Filter by slug."""

        return (
            self.published_with_related()
            .filter(
                slug=slug,
            )
        )

    def by_category(
        self,
        category: Category,
    ) -> RecipeQuerySet:
        """Filter by category."""

        return self.filter(
            category=category,
        )

    def by_category_slug(
        self,
        slug: str,
    ) -> RecipeQuerySet:
        """Filter by category slug."""

        return self.filter(
            category__slug=slug,
        )

    def by_province(
        self,
        province: Province,
    ) -> RecipeQuerySet:
        """Filter by province."""

        return self.filter(
            province=province,
        )

    def by_province_slug(
        self,
        slug: str,
    ) -> RecipeQuerySet:
        """Filter by province slug."""

        return self.filter(
            province__slug=slug,
        )

    def by_difficulty(
        self,
        difficulty: str,
    ) -> RecipeQuerySet:
        """Filter by difficulty."""

        if not difficulty:
            return self

        return self.filter(
            difficulty=difficulty,
        )

    def related(
        self,
        recipe: Recipe,
        limit: int = 6,
    ) -> RecipeQuerySet:
        """Return related recipes."""

        return (
            self.published_with_related()
            .filter(
                province=recipe.province,
            )
            .exclude(
                pk=recipe.pk,
            )
            .sort_by(
                "popular",
            )[:limit]
        )

    def sort_by(
        self,
        ordering: str = "latest",
    ) -> RecipeQuerySet:
        """Apply ordering."""

        if ordering == "oldest":
            return self.order_by(
                "published_at",
                "created_at",
            )

        if ordering == "popular":
            return self.order_by(
                "-favorite_count",
                "-view_count",
            )

        if ordering == "rating":
            return self.order_by(
                "-average_rating",
                "-rating_count",
            )

        if ordering == "title":
            return self.order_by(
                "title",
            )

        return self.order_by(
            "-published_at",
            "-created_at",
        )

    def search(
        self,
        query: str,
    ) -> RecipeQuerySet:
        """Search recipes."""

        query = query.strip()

        if not query:
            return self

        return (
            self.filter(
                Q(title__icontains=query)
                | Q(summary__icontains=query)
                | Q(category__name__icontains=query)
                | Q(province__name__icontains=query)
            )
            .distinct()
        )


class RecipeManager(models.Manager.from_queryset(RecipeQuerySet)):  # type: ignore[misc]
    """Custom manager for Recipe."""

    pass
