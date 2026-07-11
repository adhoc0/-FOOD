from __future__ import annotations

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    """Recipe tag."""

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=120,
        unique=True,
        db_index=True,
    )

    color = models.CharField(
        verbose_name=_("Color"),
        max_length=7,
        default="#4CAF50",
    )

    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        db_index=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

        ordering = [
              "name",
        ]

        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active"]),
        ]

    class Meta:    
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")

        ordering = [
            "name",
        ]

        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active"]),
        ]   

    
    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.name,
                allow_unicode=True,
            )

        super().save(*args, **kwargs)