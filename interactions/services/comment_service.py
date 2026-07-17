"""
Business logic for comments.

Yorum ekleme, onaylama ve doğrulama iş kuralları.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import transaction
from django.db.models import QuerySet

from interactions.models import Comment
from interactions.validators import CommentValidator
from recipes.models import Recipe

if TYPE_CHECKING:
    from django.contrib.auth.models import AbstractUser


class CommentService:
    """Business logic for comments."""

    @staticmethod
    @transaction.atomic
    def create(
        user: AbstractUser,
        recipe: Recipe,
        content: str,
    ) -> Comment:
        """
        Yorum oluşturur.

        Doğrulama kuralları:
        - İçerik uzunluğu kontrolü
        - Spam koruması (cooldown)

        Yeni yorumlar admin onayı bekler (is_approved=False).
        """
        CommentValidator.validate_content(content)
        CommentValidator.validate_cooldown(user, Comment)

        return Comment.objects.create(
            user=user,
            recipe=recipe,
            content=content.strip(),
            is_approved=False,
        )

    @staticmethod
    def get_approved_comments(recipe: Recipe) -> QuerySet[Comment]:
        """Onaylanmış yorumlar — optimize edilmiş."""
        return (
            Comment.objects.filter(
                recipe=recipe,
                is_approved=True,
            )
            .select_related("user")
            .order_by("-created_at")
        )

    @staticmethod
    def get_comment_count(recipe: Recipe) -> int:
        """Onaylanmış yorum sayısı."""
        return Comment.objects.filter(
            recipe=recipe,
            is_approved=True,
        ).count()
