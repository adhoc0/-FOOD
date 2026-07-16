from __future__ import annotations

from django.db import transaction

from recipes.models.recipe import Recipe
from recipes.models.recipe_image import RecipeImage
from recipes.validators import ImageValidator


class RecipeImageService:
    """Service layer responsible for RecipeImage write operations."""

    @staticmethod
    @transaction.atomic
    def create(**data) -> RecipeImage:
        """Create a new recipe image."""

        if data.get("image") is not None:
            ImageValidator.validate_image(data["image"])

        if data.get("is_cover", False):
            recipe = data["recipe"]
            RecipeImageService._clear_cover_for_recipe(recipe)

        return RecipeImage.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def update(
        recipe_image: RecipeImage,
        **data,
    ) -> RecipeImage:
        """Update recipe image fields."""

        if not data:
            return recipe_image

        if data.get("image") is not None:
            ImageValidator.validate_image(data["image"])

        target_recipe = data.get("recipe", recipe_image.recipe)
        will_be_cover = data.get("is_cover", recipe_image.is_cover)

        if will_be_cover:
            RecipeImageService._clear_cover_for_recipe(
                recipe=target_recipe,
                excluded_image_id=recipe_image.pk,
            )

        update_fields: list[str] = []

        for field, value in data.items():
            setattr(recipe_image, field, value)
            update_fields.append(field)

        if "updated_at" not in update_fields:
            update_fields.append("updated_at")

        recipe_image.save(update_fields=update_fields)

        return recipe_image

    @staticmethod
    @transaction.atomic
    def set_cover(
        recipe_image: RecipeImage,
    ) -> RecipeImage:
        """Set the image as the recipe cover."""

        RecipeImageService._set_cover(recipe_image)

        return recipe_image

    @staticmethod
    @transaction.atomic
    def unset_cover(
        recipe_image: RecipeImage,
    ) -> RecipeImage:
        """Remove cover status from the image."""

        recipe_image.is_cover = False

        recipe_image.save(
            update_fields=[
                "is_cover",
                "updated_at",
            ],
        )

        return recipe_image

    @staticmethod
    @transaction.atomic
    def delete(
        recipe_image: RecipeImage,
    ) -> None:
        """Delete the recipe image."""

        recipe_image.delete()

    @staticmethod
    def _set_cover(
        recipe_image: RecipeImage,
    ) -> None:
        """Ensure only one cover image exists per recipe."""

        RecipeImageService._clear_cover_for_recipe(
            recipe=recipe_image.recipe,
            excluded_image_id=recipe_image.pk,
        )

        recipe_image.is_cover = True
        recipe_image.save(
            update_fields=[
                "is_cover",
                "updated_at",
            ],
        )

    @staticmethod
    def _clear_cover_for_recipe(
        recipe: Recipe,
        excluded_image_id: int | None = None,
    ) -> None:
        """Tarif kilidi altında mevcut kapak görsellerini kaldırır."""

        Recipe.objects.select_for_update().get(pk=recipe.pk)

        cover_images = RecipeImage.objects.filter(
            recipe=recipe,
            is_cover=True,
        )

        if excluded_image_id is not None:
            cover_images = cover_images.exclude(pk=excluded_image_id)

        cover_images.update(is_cover=False)
