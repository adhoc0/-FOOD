from recipes.models import Ingredient


class IngredientService:
    """Business logic for ingredients."""

    @staticmethod
    def get_or_create(name: str):
        ingredient, _ = Ingredient.objects.get_or_create(
            name=name.strip(),
        )

        return ingredient