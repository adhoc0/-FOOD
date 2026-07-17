from __future__ import annotations

from typing import ClassVar

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from provinces.managers.region_manager import RegionManager


class Region(models.Model):
    """Region model."""

    objects: ClassVar[RegionManager] = RegionManager()

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=50,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=60,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    map_color = models.CharField(
        verbose_name=_("Map Color"),
        max_length=7,
        default="#2E7D32",
        help_text=_("HEX color code (#RRGGBB)."),
    )

    display_order = models.PositiveSmallIntegerField(
        verbose_name=_("Display Order"),
        default=1,
        db_index=True,
    )

    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        db_index=True,
    )

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

        ordering = [
            "display_order",
            "name",
        ]

        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["display_order"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse(
            "provinces:list",
        ) + f"?region={self.slug}"
