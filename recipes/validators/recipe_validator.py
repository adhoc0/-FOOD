from django.core.exceptions import ValidationError


class RecipeValidator:
    """Recipe business validations."""

    @staticmethod
    def validate_preparation_time(value: int):
        if value < 0:
            raise ValidationError(
                "Hazırlık süresi negatif olamaz."
            )

    @staticmethod
    def validate_cooking_time(value: int):
        if value < 0:
            raise ValidationError(
                "Pişirme süresi negatif olamaz."
            )

    @staticmethod
    def validate_servings(value: int):
        if value < 1:
            raise ValidationError(
                "Porsiyon en az 1 olmalıdır."
            )

    @staticmethod
    def validate_summary(value: str):
        if len(value.strip()) < 30:
            raise ValidationError(
                "Özet en az 30 karakter olmalıdır."
            )

    @staticmethod
    def validate_title(value: str):
        if len(value.strip()) < 3:
            raise ValidationError(
                "Başlık çok kısa."
            )