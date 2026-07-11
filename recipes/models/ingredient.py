from __future__ import annotations

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    """Recipe ingredient."""

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=150,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=170,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
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
        ordering = [
            "name",
        ]
        verbose_name = _("Ingredient")
        verbose_name_plural = _("Ingredients")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.name,
                allow_unicode=True,
            )

        super().save(*args, **kwargs)