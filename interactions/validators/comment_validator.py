"""
Comment validations.

Yorum içeriğinin güvenlik ve kalite kontrolünü sağlar.
Spam koruması için zaman bazlı kontrol içerir.
"""

from __future__ import annotations

from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    COMMENT_COOLDOWN_SECONDS,
    MAX_COMMENT_LENGTH,
    MIN_COMMENT_LENGTH,
)


class CommentValidator:
    """Comment validations."""

    @staticmethod
    def validate_content(value: str) -> None:
        """Yorum içerik doğrulaması."""
        stripped = value.strip()

        if len(stripped) < MIN_COMMENT_LENGTH:
            raise ValidationError(
                _("Yorum en az %(min)d karakter olmalıdır."),
                params={"min": MIN_COMMENT_LENGTH},
            )

        if len(stripped) > MAX_COMMENT_LENGTH:
            raise ValidationError(
                _("Yorum en fazla %(max)d karakter olabilir."),
                params={"max": MAX_COMMENT_LENGTH},
            )

    @staticmethod
    def validate_cooldown(user, comment_model) -> None:
        """
        Spam koruması: Aynı kullanıcının kısa sürede tekrar yorum yapmasını engeller.

        comment_model parametresi interactions.models.Comment sınıfıdır.
        Circular import'u önlemek için model dışarıdan geçilir.
        """
        from datetime import timedelta

        cooldown_threshold = timezone.now() - timedelta(seconds=COMMENT_COOLDOWN_SECONDS)

        recent_comment_exists = (
            comment_model.objects.filter(
                user=user,
                created_at__gte=cooldown_threshold,
            ).exists()
        )

        if recent_comment_exists:
            raise ValidationError(
                _("Çok sık yorum yapıyorsunuz. Lütfen %(seconds)d saniye bekleyin."),
                params={"seconds": COMMENT_COOLDOWN_SECONDS},
            )
