from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from .recipe import Recipe
from .tag import Tag


class RecipeTag(models.Model):
    """Recipe tag relation."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="tags",
    )

    tag = models.ForeignKey(
        Tag,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _("Recipe Tag")
        verbose_name_plural = _("Recipe Tags")

        ordering = [
            "tag__name",
        ]

        indexes = [
            models.Index(fields=["recipe"]),
            models.Index(fields=["tag"]),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "recipe",
                    "tag",
                ],
                name="unique_recipe_tag",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.recipe} - {self.tag}"