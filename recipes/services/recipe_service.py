from __future__ import annotations

from django.db import transaction
from django.db.models import F
from django.utils import timezone

from recipes.choices import Status
from recipes.models import Recipe


class RecipeService:
    """Service layer responsible for Recipe write operations."""

    @staticmethod
    @transaction.atomic
    def create(**data) -> Recipe:
        """Create a new recipe."""

        return Recipe.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def update(
        recipe: Recipe,
        **data,
    ) -> Recipe:
        """Update recipe fields."""

        if not data:
            return recipe

        update_fields: list[str] = []

        for field, value in data.items():
            setattr(recipe, field, value)
            update_fields.append(field)

        recipe.save(update_fields=update_fields)

        return recipe

    @staticmethod
    @transaction.atomic
    def publish(
        recipe: Recipe,
    ) -> Recipe:
        """Publish the recipe."""

        recipe.status = Status.PUBLISHED
        recipe.published_at = timezone.now()

        recipe.save(
            update_fields=[
                "status",
                "published_at",
            ],
        )

        return recipe

    @staticmethod
    @transaction.atomic
    def unpublish(
        recipe: Recipe,
    ) -> Recipe:
        """Unpublish the recipe."""

        recipe.status = Status.DRAFT
        recipe.published_at = None

        recipe.save(
            update_fields=[
                "status",
                "published_at",
            ],
        )

        return recipe

    @staticmethod
    @transaction.atomic
    def activate(
        recipe: Recipe,
    ) -> Recipe:
        """Activate the recipe."""

        return RecipeService._set_active(
            recipe=recipe,
            is_active=True,
        )

    @staticmethod
    @transaction.atomic
    def deactivate(
        recipe: Recipe,
    ) -> Recipe:
        """Deactivate the recipe."""

        return RecipeService._set_active(
            recipe=recipe,
            is_active=False,
        )

    @staticmethod
    @transaction.atomic
    def feature(
        recipe: Recipe,
    ) -> Recipe:
        """Mark the recipe as featured."""

        return RecipeService._set_featured(
            recipe=recipe,
            is_featured=True,
        )

    @staticmethod
    @transaction.atomic
    def unfeature(
        recipe: Recipe,
    ) -> Recipe:
        """Remove featured status from the recipe."""

        return RecipeService._set_featured(
            recipe=recipe,
            is_featured=False,
        )

    @staticmethod
    @transaction.atomic
    def increment_view_count(
        recipe: Recipe,
    ) -> None:
        """Increment recipe view count."""

        Recipe.objects.filter(
            pk=recipe.pk,
        ).update(
            view_count=F("view_count") + 1,
        )

        recipe.refresh_from_db(
            fields=[
                "view_count",
            ],
        )

    @staticmethod
    @transaction.atomic
    def increment_favorite_count(
        recipe: Recipe,
    ) -> None:
        """Increment recipe favorite count."""

        Recipe.objects.filter(
            pk=recipe.pk,
        ).update(
            favorite_count=F("favorite_count") + 1,
        )

        recipe.refresh_from_db(
            fields=[
                "favorite_count",
            ],
        )

    @staticmethod
    @transaction.atomic
    def decrement_favorite_count(
        recipe: Recipe,
    ) -> None:
        """Decrement recipe favorite count."""

        Recipe.objects.filter(
            pk=recipe.pk,
            favorite_count__gt=0,
        ).update(
            favorite_count=F("favorite_count") - 1,
        )

        recipe.refresh_from_db(
            fields=[
                "favorite_count",
            ],
        )

    @staticmethod
    @transaction.atomic
    def delete(
        recipe: Recipe,
    ) -> None:
        """Delete the recipe."""

        recipe.delete()

    @staticmethod
    def _set_active(
        *,
        recipe: Recipe,
        is_active: bool,
    ) -> Recipe:
        """Update recipe active status."""

        recipe.is_active = is_active

        recipe.save(
            update_fields=[
                "is_active",
            ],
        )

        return recipe

    @staticmethod
    def _set_featured(
        *,
        recipe: Recipe,
        is_featured: bool,
    ) -> Recipe:
        """Update recipe featured status."""

        recipe.is_featured = is_featured

        recipe.save(
            update_fields=[
                "is_featured",
            ],
        )

        return recipe
