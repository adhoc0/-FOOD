from __future__ import annotations

from django.db.models import QuerySet

from accounts.models import CustomUser
from interactions.models import Comment, Favorite


class ProfileSelector:
    """Profil ekranı için yalnızca okuma sorguları."""

    @staticmethod
    def get_favorites(user: CustomUser) -> QuerySet[Favorite]:
        return (
            Favorite.objects.filter(user=user)
            .select_related(
                "recipe",
                "recipe__province",
                "recipe__category",
            )
            .order_by("-created_at")
        )

    @staticmethod
    def get_comments(user: CustomUser) -> QuerySet[Comment]:
        return (
            Comment.objects.filter(user=user)
            .select_related("recipe", "recipe__province")
            .order_by("-created_at")
        )
