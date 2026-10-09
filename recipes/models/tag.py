from __future__ import annotations

from typing import ClassVar

from django.db import models
from django.utils.translation import gettext_lazy as _

from recipes.querysets.tag_queryset import TagManager


class Tag(models.Model):
    """Tag model."""

    objects: ClassVar[TagManager] = TagManager()

    name = models.CharField(
        _("Name"),
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        _("Slug"),
        max_length=120,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        _("Description"),
        blank=True,
    )

    is_active = models.BooleanField(
        _("Active"),
        default=True,
        db_index=True,
    )

    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

        ordering = [
            "name",
        ]

        indexes = [
            models.Index(
                fields=[
                    "slug",
                ],
            ),
            models.Index(
                fields=[
                    "is_active",
                ],
            ),
        ]

    def __str__(self) -> str:
        return self.name
