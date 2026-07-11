from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from .ingredient import Ingredient
from .recipe import Recipe


class Unit(models.TextChoices):
    GRAM = "g", _("Gram")
    KILOGRAM = "kg", _("Kilogram")
    MILLILITER = "ml", _("Milliliter")
    LITER = "l", _("Liter")
    TEASPOON = "tsp", _("Tea Spoon")
    TABLESPOON = "tbsp", _("Table Spoon")
    CUP = "cup", _("Cup")
    PIECE = "piece", _("Piece")
    PINCH = "pinch", _("Pinch")
    OPTIONAL = "optional", _("Optional")


class RecipeIngredient(models.Model):
    """Recipe ingredient."""

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredients",
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    quantity = models.DecimalField(
        _("Quantity"),
        max_digits=8,
        decimal_places=2,
    )

    unit = models.CharField(
        _("Unit"),
        max_length=20,
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

    class Meta:
        verbose_name = _("Recipe Ingredient")
        verbose_name_plural = _("Recipe Ingredients")

        ordering = [
            "sort_order",
            "id",
        ]

        indexes = [
            models.Index(fields=["recipe"]),
            models.Index(fields=["ingredient"]),
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