"""
Business logic for ratings.

Handles rating operations and keeps recipe rating statistics synchronized.
"""

from __future__ import annotations

from decimal import Decimal

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Avg, Count

from common.types import UserLike
from interactions.models import Rating
from recipes.models import Recipe


class RatingService:
    """Service layer responsible for rating operations."""

    @staticmethod
    @transaction.atomic
    def rate(
        user: UserLike,
        recipe: Recipe,
        score: int,
    ) -> Rating:
        """
        Create or update a user's rating for a recipe.
        """

        if not isinstance(score, int) or not 1 <= score <= 5:
            raise ValidationError("Puan 1 ile 5 arasında olmalıdır.")

        rating, _ = Rating.objects.update_or_create(
            user=user,
            recipe=recipe,
            defaults={
                "score": score,
            },
        )

        RatingService._refresh_recipe_rating(recipe)

        return rating

    @staticmethod
    def get_average_rating(
        recipe: Recipe,
    ) -> Decimal:
        """
        Return the cached average rating.
        """
        recipe.refresh_from_db(fields=["average_rating"])
        return recipe.average_rating

    @staticmethod
    def get_rating_count(
        recipe: Recipe,
    ) -> int:
        """
        Return the cached rating count.
        """
        recipe.refresh_from_db(fields=["rating_count"])
        return recipe.rating_count

    @staticmethod
    def get_user_rating(
        user: UserLike,
        recipe: Recipe,
    ) -> int | None:
        """
        Return the user's rating for the recipe.

        Returns None if the user has not rated the recipe.
        """

        if not user.is_authenticated:
            return None

        return (
            Rating.objects.filter(
                user=user,
                recipe=recipe,
            )
            .values_list(
                "score",
                flat=True,
            )
            .first()
        )

    @staticmethod
    def _refresh_recipe_rating(
        recipe: Recipe,
    ) -> None:
        """
        Synchronize cached rating statistics on the recipe.
        """

        statistics = Rating.objects.filter(
            recipe=recipe,
        ).aggregate(
            average=Avg("score"),
            count=Count("id"),
        )

        recipe.average_rating = (
            Decimal(str(statistics["average"])).quantize(
                Decimal("0.1"),
            )
            if statistics["average"] is not None
            else Decimal("0")
        )

        recipe.rating_count = statistics["count"] or 0

        recipe.save(
            update_fields=[
                "average_rating",
                "rating_count",
            ],
        )
