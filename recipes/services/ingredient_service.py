from __future__ import annotations

from django.db import transaction

from recipes.models.ingredient import Ingredient


class IngredientService:
    """Service layer responsible for Ingredient write operations."""

    @staticmethod
    @transaction.atomic
    def create(**data) -> Ingredient:
        """Create a new ingredient."""

        return Ingredient.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def update(
        ingredient: Ingredient,
        **data,
    ) -> Ingredient:
        """Update ingredient fields."""

        if not data:
            return ingredient

        update_fields: list[str] = []

        for field, value in data.items():
            setattr(ingredient, field, value)
            update_fields.append(field)

        ingredient.save(update_fields=update_fields)

        return ingredient

    @staticmethod
    @transaction.atomic
    def activate(
        ingredient: Ingredient,
    ) -> Ingredient:
        """Activate the ingredient."""

        return IngredientService._set_active(
            ingredient=ingredient,
            is_active=True,
        )

    @staticmethod
    @transaction.atomic
    def deactivate(
        ingredient: Ingredient,
    ) -> Ingredient:
        """Deactivate the ingredient."""

        return IngredientService._set_active(
            ingredient=ingredient,
            is_active=False,
        )

    @staticmethod
    @transaction.atomic
    def delete(
        ingredient: Ingredient,
    ) -> None:
        """Delete the ingredient."""

        ingredient.delete()

    @staticmethod
    def _set_active(
        *,
        ingredient: Ingredient,
        is_active: bool,
    ) -> Ingredient:
        """Update ingredient active status."""

        ingredient.is_active = is_active

        ingredient.save(
            update_fields=[
                "is_active",
            ],
        )

        return ingredient
