from __future__ import annotations

from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .recipe import Recipe


class RecipeImage(models.Model):
    """Recipe image."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        _("Image"),
        upload_to="recipes/",
    )

    alt_text = models.CharField(
        _("Alt Text"),
        max_length=255,
    )

    is_cover = models.BooleanField(
        _("Cover Image"),
        default=False,
        db_index=True,
    )

    sort_order = models.PositiveSmallIntegerField(
        _("Sort Order"),
        default=0,
        db_index=True,
    )

    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Recipe Image")
        verbose_name_plural = _("Recipe Images")

        ordering = [
            "sort_order",
            "id",
        ]

        indexes = [
            models.Index(fields=["recipe"]),
            models.Index(fields=["is_cover"]),
            models.Index(fields=["sort_order"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["recipe"],
                condition=Q(is_cover=True),
                name="unique_cover_image_per_recipe",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.recipe} ({self.sort_order})"