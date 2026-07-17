from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from recipes.choices import Unit

from .ingredient import Ingredient
from .recipe import Recipe


class RecipeIngredient(models.Model):
    """Intermediate model between Recipe and Ingredient."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients",
        verbose_name=_("Recipe"),
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        related_name="recipe_ingredients",
        verbose_name=_("Ingredient"),
    )

    quantity = models.DecimalField(
        _("Quantity"),
        max_digits=8,
        decimal_places=2,
    )

    unit = models.CharField(
        _("Unit"),
        max_length=10,
        choices=Unit.choices,
        default=Unit.GRAM,
    )

    note = models.CharField(
        _("Note"),
        max_length=255,
        blank=True,
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

    updated_at = models.DateTimeField(
        _("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Recipe Ingredient")
        verbose_name_plural = _("Recipe Ingredients")

        ordering = [
            "sort_order",
            "id",
        ]

        indexes = [
            models.Index(
                fields=[
                    "recipe",
                ],
            ),
            models.Index(
                fields=[
                    "ingredient",
                ],
            ),
            models.Index(
                fields=[
                    "sort_order",
                ],
            ),
        ]

        constraints = [
            models.UniqueConstraint(
                fields=[
                    "recipe",
                    "ingredient",
                ],
                name="unique_recipe_ingredient",
            ),
        ]

    def __str__(self) -> str:
        return (
            f"{self.recipe} - "
            f"{self.quantity} {self.unit} "
            f"{self.ingredient}"
        )
