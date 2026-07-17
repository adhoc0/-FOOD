from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager


class CustomUser(AbstractUser):
    """Custom user model."""

    objects = UserManager()

    email = models.EmailField(
        _("Email Address"),
        unique=True,
        db_index=True,
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

        ordering = [
            "-date_joined",
        ]

        indexes = [
            models.Index(fields=["email"]),
            models.Index(fields=["date_joined"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self) -> str:
        full_name = self.get_full_name()

        return full_name if full_name else self.username
