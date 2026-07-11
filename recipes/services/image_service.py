from recipes.models import Recipe, RecipeImage


class ImageService:
    """Business logic for recipe images."""

    @staticmethod
    def add_image(
        recipe: Recipe,
        image,
        alt_text: str,
        is_cover: bool = False,
    ):
        return RecipeImage.objects.create(
            recipe=recipe,
            image=image,
            alt_text=alt_text,
            is_cover=is_cover,
        )