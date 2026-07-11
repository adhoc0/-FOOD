from __future__ import annotations

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Category(models.Model):
    """Recipe category."""

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

    image = models.ImageField(
        verbose_name=_("Image"),
        upload_to="categories/",
        blank=True,
        null=True,
    )

    icon = models.CharField(
        verbose_name=_("Icon"),
        max_length=100,
        blank=True,
    )

    sort_order = models.PositiveSmallIntegerField(
        verbose_name=_("Sort Order"),
        default=0,
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
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

        ordering = [
            "sort_order",
            "name",
        ]

        indexes = [
            models.Index(fields=["slug"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["sort_order"]),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse(
            "recipes:category_detail",
            kwargs={"slug": self.slug},
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.name,
                allow_unicode=True,
            )

        super().save(*args, **kwargs)