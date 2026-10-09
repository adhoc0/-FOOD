from __future__ import annotations

from django.conf import settings
from django.db import models


class TOTPDevice(models.Model):
    """Kullanıcının iki adımlı doğrulama (TOTP) cihazı."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="totp_device",
    )
    secret = models.CharField(max_length=64, editable=False)
    confirmed = models.BooleanField(default=False)
    last_used_step = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"TOTP({self.user_id}, confirmed={self.confirmed})"
