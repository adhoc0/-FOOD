from __future__ import annotations

from django.db import models


class UserQuerySet(models.QuerySet):
    """Custom QuerySet for users."""

    def active(self) -> UserQuerySet:
        return self.filter(
            is_active=True,
        )

    def staff(self) -> UserQuerySet:
        return self.active().filter(
            is_staff=True,
        )

    def superusers(self) -> UserQuerySet:
        return self.filter(
            is_superuser=True,
        )

    def order_by_default(self) -> UserQuerySet:
        return self.order_by(
            "date_joined",
        )

    def by_username(
        self,
        username: str,
    ) -> UserQuerySet:
        return self.active().filter(
            username=username,
        )

    def by_email(
        self,
        email: str,
    ) -> UserQuerySet:
        return self.active().filter(
            email=email,
        )
