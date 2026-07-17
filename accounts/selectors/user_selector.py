from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db.models import QuerySet

User = get_user_model()


class UserSelector:
    """Read-only queries for users."""

    @staticmethod
    def get_queryset() -> QuerySet:
        return User.objects.active().order_by_default()

    @classmethod
    def get_all(cls) -> QuerySet:
        return cls.get_queryset()

    @classmethod
    def get_by_id(
        cls,
        user_id: int,
    ):
        return (
            cls.get_queryset()
            .filter(
                id=user_id,
            )
            .first()
        )

    @classmethod
    def get_by_username(
        cls,
        username: str,
    ):
        return User.objects.by_username(username).first()

    @classmethod
    def get_by_email(
        cls,
        email: str,
    ):
        return User.objects.by_email(email).first()

    @classmethod
    def get_staff(cls) -> QuerySet:
        return User.objects.staff().order_by_default()

    @classmethod
    def get_count(cls) -> int:
        return User.objects.active().count()
