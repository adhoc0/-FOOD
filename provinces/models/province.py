from __future__ import annotations

from typing import ClassVar

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from provinces.managers.province_manager import ProvinceManager

from .region import Region


class Province(models.Model):
    """Türkiye'deki illeri temsil eder."""

    objects: ClassVar[ProvinceManager] = ProvinceManager()

    region = models.ForeignKey(
        Region,
        verbose_name=_("Region"),
        on_delete=models.PROTECT,
        related_name="provinces",
    )

    plate_code = models.PositiveSmallIntegerField(
        verbose_name=_("Plate Code"),
        unique=True,
        db_index=True,
    )

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

    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    latitude = models.DecimalField(
        verbose_name=_("Latitude"),
        max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        verbose_name=_("Longitude"),
        max_digits=9,
        decimal_places=6,
    )

    map_x = models.DecimalField(
        verbose_name=_("Map X"),
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    map_y = models.DecimalField(
        verbose_name=_("Map Y"),
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    is_featured = models.BooleanField(
        verbose_name=_("Featured"),
        default=False,
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
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")

        ordering = [
            "plate_code",
        ]

        indexes = [
            models.Index(fields=["region"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["plate_code"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["is_featured"]),
            models.Index(fields=["region", "is_active"]),
        ]

    def __str__(self) -> str:
        return f"{self.plate_code:02d} - {self.name}"

    def get_absolute_url(self) -> str:
        return reverse(
            "provinces:detail",
            kwargs={
                "slug": self.slug,
            },
        )
