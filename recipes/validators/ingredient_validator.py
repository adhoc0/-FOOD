from django.core.exceptions import ValidationError


class IngredientValidator:
    """Ingredient validations."""

    @staticmethod
    def validate_name(value: str):
        if len(value.strip()) < 2:
            raise ValidationError(
                "Malzeme adı çok kısa."
            )