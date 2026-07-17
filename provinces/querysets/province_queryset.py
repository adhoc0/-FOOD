from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

if TYPE_CHECKING:
    from provinces.models import Province  # noqa: F401


class ProvinceQuerySet(models.QuerySet["Province"]):
    """Custom QuerySet for Province."""

    def active(self) -> ProvinceQuerySet:
        """Return active provinces."""
        return self.filter(
            is_active=True,
        )

    def inactive(self) -> ProvinceQuerySet:
        """Return inactive provinces."""
        return self.filter(
            is_active=False,
        )

    def featured(self) -> ProvinceQuerySet:
        """Return featured provinces."""
        return self.filter(
            is_featured=True,
        )

    def ordered_by_code(self) -> ProvinceQuerySet:
        """Order provinces by plate code."""
        return self.order_by(
            "plate_code",
        )

    def sort_by_name(self) -> ProvinceQuerySet:
        """Order provinces alphabetically."""
        return self.order_by(
            "name",
        )

    def with_related(self) -> ProvinceQuerySet:
        """Load related objects."""
        return self.select_related(
            "region",
        )

    def by_slug(
        self,
        slug: str,
    ) -> ProvinceQuerySet:
        """Filter by slug."""
        return self.filter(
            slug=slug,
        )

    def by_plate_code(
        self,
        plate_code: int,
    ) -> ProvinceQuerySet:
        """Filter by plate code."""
        return self.filter(
            plate_code=plate_code,
        )

    def by_region(
        self,
        region,
    ) -> ProvinceQuerySet:
        """Filter by region."""
        return self.filter(
            region=region,
        )

    def search(
        self,
        query: str,
    ) -> ProvinceQuerySet:
        """Search provinces."""

        query = query.strip()

        if not query:
            return self

        return self.filter(
            models.Q(name__icontains=query)
            | models.Q(slug__icontains=query)
        )

    def with_recipe_count(self) -> ProvinceQuerySet:
        """Annotate recipe count."""

        return self.annotate(
            recipe_count=models.Count(
                "recipes",
                distinct=True,
            ),
        )

    def has_recipes(self) -> ProvinceQuerySet:
        """Return provinces containing recipes."""

        return (
            self.with_recipe_count()
            .filter(
                recipe_count__gt=0,
            )
        )

    def active_with_recipe_count(self) -> ProvinceQuerySet:
        """Return active provinces with recipe counts."""

        return (
            self.active()
            .with_recipe_count()
            .sort_by_name()
        )

    def active_with_recipes(self) -> ProvinceQuerySet:
        """Return active provinces containing recipes."""

        return (
            self.active()
            .has_recipes()
            .sort_by_name()
        )


class ProvinceManager(models.Manager.from_queryset(ProvinceQuerySet)):  # type: ignore[misc]
    """Custom manager for Province."""

    pass
