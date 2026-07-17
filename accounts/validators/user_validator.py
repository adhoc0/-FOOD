from __future__ import annotations

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


def validate_unique_email(
    email: str,
) -> None:
    """Validate email uniqueness."""

    if User.objects.filter(
        email__iexact=email,
    ).exists():
        raise ValidationError(
            _("A user with this email already exists."),
        )


def validate_username(
    username: str,
) -> None:
    """Validate username."""

    if len(username) < 3:
        raise ValidationError(
            _("Username must contain at least 3 characters."),
        )
