"""
Business logic for favorites.

Handles favorite create/remove operations and keeps recipe counters synchronized.
"""

from __future__ import annotations

from django.db import transaction
from django.db.models import F, QuerySet

from common.types import UserLike
from interactions.models import Favorite
from recipes.models import Recipe


class FavoriteService:
    """Service layer responsible for favorite operations."""

    @staticmethod
    @transaction.atomic
    def toggle(
        user: UserLike,
        recipe: Recipe,
    ) -> bool:
        """
        Toggle recipe favorite status.

        Returns:
            True: Recipe was added to favorites.
            False: Recipe was removed from favorites.
        """

        favorite, created = Favorite.objects.get_or_create(
            user=user,
            recipe=recipe,
        )

        if created:
            FavoriteService._increment_recipe_count(recipe)
            return True

        favorite.delete()
        FavoriteService._decrement_recipe_count(recipe)

        return False

    @staticmethod
    def is_favorited(
        user: UserLike,
        recipe: Recipe,
    ) -> bool:
        """Return whether the recipe is favorited by the user."""

        if not user.is_authenticated:
            return False

        return Favorite.objects.filter(
            user=user,
            recipe=recipe,
        ).exists()

    @staticmethod
    def get_user_favorites(
        user: UserLike,
    ) -> QuerySet[Favorite]:
        """Return optimized queryset of user's favorites."""

        return (
            Favorite.objects.filter(
                user=user,
            )
            .select_related(
                "recipe",
                "recipe__province",
                "recipe__category",
            )
            .order_by(
                "-created_at",
            )
        )

    @staticmethod
    def _increment_recipe_count(
        recipe: Recipe,
    ) -> None:
        """Increment recipe favorite counter."""

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
    def _decrement_recipe_count(
        recipe: Recipe,
    ) -> None:
        """Decrement recipe favorite counter."""

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
