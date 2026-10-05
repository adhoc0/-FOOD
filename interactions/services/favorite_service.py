"""
Business logic for favorites.

Handles favorite create/remove operations and keeps recipe counters synchronized.
"""

from __future__ import annotations

from django.db import transaction
from django.db.models import QuerySet

from common.types import UserLike
from interactions.models import Favorite
from recipes.models import Recipe
from recipes.services.recipe_service import RecipeService


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

        favorite, created = Favorite.objects.get_or_create(  # type: ignore[misc]
            user=user,
            recipe=recipe,
        )

        if created:
            RecipeService.increment_favorite_count(recipe)
            return True

        favorite.delete()
        RecipeService.decrement_favorite_count(recipe)

        return False

    @staticmethod
    def is_favorited(
        user: UserLike,
        recipe: Recipe,
    ) -> bool:
        """Return whether the recipe is favorited by the user."""

        if not user.is_authenticated:
            return False

        return Favorite.objects.filter(  # type: ignore[misc]
            user=user,
            recipe=recipe,
        ).exists()

    @staticmethod
    def get_user_favorites(
        user: UserLike,
    ) -> QuerySet[Favorite]:
        """Return optimized queryset of user's favorites."""

        return (
            Favorite.objects.filter(  # type: ignore[misc]
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
