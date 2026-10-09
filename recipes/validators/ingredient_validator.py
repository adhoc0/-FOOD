"""
Ingredient validations.

Provides validation rules for ingredient data.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    MAX_INGREDIENT_NAME_LENGTH,
    MAX_INGREDIENT_QUANTITY,
    MIN_INGREDIENT_NAME_LENGTH,
    MIN_INGREDIENT_QUANTITY,
)


class IngredientValidator:
    """Validation helpers for Ingredient."""

    @staticmethod
    def validate_name(value: str) -> None:
        """Validate ingredient name."""

        if not isinstance(value, str):
            raise ValidationError(
                _("Ingredient name must be a string."),
            )

        if not value.strip():
            raise ValidationError(
                _("Ingredient name cannot be empty."),
            )

        length = len(value.strip())

        if length < MIN_INGREDIENT_NAME_LENGTH:
            raise ValidationError(
                _(
                    "Ingredient name must contain at least %(min)d characters."
                ),
                params={
                    "min": MIN_INGREDIENT_NAME_LENGTH,
                },
            )

        if length > MAX_INGREDIENT_NAME_LENGTH:
            raise ValidationError(
                _(
                    "Ingredient name cannot exceed %(max)d characters."
                ),
                params={
                    "max": MAX_INGREDIENT_NAME_LENGTH,
                },
            )

    @staticmethod
    def validate_quantity(
        value: Decimal | int | float | str,
    ) -> None:
        """Validate ingredient quantity."""

        try:
            quantity = Decimal(str(value))
        except (InvalidOperation, TypeError, ValueError) as exc:
            raise ValidationError(
                _("Invalid ingredient quantity."),
            ) from exc

        if quantity.is_nan():
            raise ValidationError(
                _("Ingredient quantity cannot be NaN."),
            )

        if quantity.is_infinite():
            raise ValidationError(
                _("Ingredient quantity cannot be infinite."),
            )

        if quantity < MIN_INGREDIENT_QUANTITY:
            raise ValidationError(
                _(
                    "Ingredient quantity cannot be less than %(min)s."
                ),
                params={
                    "min": MIN_INGREDIENT_QUANTITY,
                },
            )

        if quantity > MAX_INGREDIENT_QUANTITY:
            raise ValidationError(
                _(
                    "Ingredient quantity cannot exceed %(max)s."
                ),
                params={
                    "max": MAX_INGREDIENT_QUANTITY,
                },
            )
