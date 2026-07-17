from __future__ import annotations

from django.db import transaction

from recipes.models.cuisine import Cuisine


class CuisineService:
    """Service layer responsible for Cuisine write operations."""

    @staticmethod
    @transaction.atomic
    def create(**data) -> Cuisine:
        """Create a new cuisine."""

        return Cuisine.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def update(
        cuisine: Cuisine,
        **data,
    ) -> Cuisine:
        """Update cuisine fields."""

        if not data:
            return cuisine

        update_fields: list[str] = []

        for field, value in data.items():
            setattr(cuisine, field, value)
            update_fields.append(field)

        cuisine.save(update_fields=update_fields)

        return cuisine

    @staticmethod
    @transaction.atomic
    def activate(
        cuisine: Cuisine,
    ) -> Cuisine:
        """Activate the cuisine."""

        return CuisineService._set_active(
            cuisine=cuisine,
            is_active=True,
        )

    @staticmethod
    @transaction.atomic
    def deactivate(
        cuisine: Cuisine,
    ) -> Cuisine:
        """Deactivate the cuisine."""

        return CuisineService._set_active(
            cuisine=cuisine,
            is_active=False,
        )

    @staticmethod
    @transaction.atomic
    def delete(
        cuisine: Cuisine,
    ) -> None:
        """Delete the cuisine."""

        cuisine.delete()

    @staticmethod
    def _set_active(
        *,
        cuisine: Cuisine,
        is_active: bool,
    ) -> Cuisine:
        """Update cuisine active status."""

        cuisine.is_active = is_active

        cuisine.save(
            update_fields=[
                "is_active",
            ],
        )

        return cuisine
