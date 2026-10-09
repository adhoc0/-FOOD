from __future__ import annotations

from django.contrib.auth.models import UserManager as DjangoUserManager

from .user_queryset import UserQuerySet


class UserManager(DjangoUserManager.from_queryset(UserQuerySet)):  # type: ignore[misc]
    """Custom manager for users."""

    use_in_migrations = True
