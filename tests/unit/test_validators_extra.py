"""BaseValidator.validate_decimal, IngredientValidator ve RecipeValidator ek dalları."""

from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError

from recipes.constants import (
    MAX_INGREDIENT_NAME_LENGTH,
    MAX_INGREDIENT_QUANTITY,
    MIN_INGREDIENT_NAME_LENGTH,
)
from recipes.validators.base_validator import BaseValidator
from recipes.validators.ingredient_validator import IngredientValidator
from recipes.validators.recipe_validator import RecipeValidator


class TestValidateDecimal:
    def _call(self, value):
        return BaseValidator.validate_decimal(
            value, "Miktar", Decimal("0"), Decimal("10")
        )

    def test_returns_decimal(self):
        assert self._call("2.5") == Decimal("2.5")
        assert self._call(3) == Decimal("3")

    @pytest.mark.parametrize("bad", ["abc", None, "NaN", "Infinity", "-1", "11"])
    def test_rejects_invalid(self, bad):
        with pytest.raises(ValidationError):
            self._call(bad)

    def test_boundaries(self):
        assert self._call(0) == Decimal("0")
        assert self._call(10) == Decimal("10")


class TestIngredientValidator:
    def test_name_rules(self):
        IngredientValidator.validate_name("a" * MIN_INGREDIENT_NAME_LENGTH)
        IngredientValidator.validate_name("a" * MAX_INGREDIENT_NAME_LENGTH)

        for bad in (123, "", "   ", "a" * (MIN_INGREDIENT_NAME_LENGTH - 1),
                    "a" * (MAX_INGREDIENT_NAME_LENGTH + 1)):
            with pytest.raises(ValidationError):
                IngredientValidator.validate_name(bad)

    @pytest.mark.parametrize("bad", ["abc", None, "NaN", "Infinity", -1, MAX_INGREDIENT_QUANTITY + 1])
    def test_quantity_rejects_invalid(self, bad):
        with pytest.raises(ValidationError):
            IngredientValidator.validate_quantity(bad)

    @pytest.mark.parametrize("good", [0, "1.5", MAX_INGREDIENT_QUANTITY])
    def test_quantity_accepts_valid(self, good):
        IngredientValidator.validate_quantity(good)


class TestRecipeValidatorExtra:
    def test_invalid_status_rejected(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_status("bilinmeyen")

    def test_status_transitions(self):
        RecipeValidator.validate_status_transition("draft", "draft")
        RecipeValidator.validate_status_transition("draft", "published")

        with pytest.raises(ValidationError):
            RecipeValidator.validate_status_transition("draft", "archived")

    def test_total_time_cannot_exceed_24_hours(self):
        with pytest.raises(ValidationError):
            RecipeValidator.validate_recipe_data(
                {"preparation_time": 1000, "cooking_time": 1000}
            )
