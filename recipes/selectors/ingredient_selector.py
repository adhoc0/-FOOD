from recipes.models import Ingredient


class IngredientSelector:
    """Read-only queries for ingredients."""

    @staticmethod
    def get_all():
        return (
            Ingredient.objects.filter(
                is_active=True,
            )
            .order_by(
                "name",
            )
        )

    @staticmethod
    def get_by_slug(slug: str):
        return Ingredient.objects.filter(
            slug=slug,
            is_active=True,
        ).first()

    @staticmethod
    def get_count() -> int:
        return Ingredient.objects.filter(
            is_active=True,
        ).count()