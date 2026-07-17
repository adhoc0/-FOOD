from __future__ import annotations

from django.db import transaction

from recipes.models.category import Category


class CategoryService:
    """Service layer responsible for Category write operations."""

    @staticmethod
    @transaction.atomic
    def create(**data) -> Category:
        """Create a new category."""

        return Category.objects.create(**data)

    @staticmethod
    @transaction.atomic
    def update(
        category: Category,
        **data,
    ) -> Category:
        """Update category fields."""

        if not data:
            return category

        update_fields: list[str] = []

        for field, value in data.items():
            setattr(category, field, value)
            update_fields.append(field)

        category.save(update_fields=update_fields)

        return category

    @staticmethod
    @transaction.atomic
    def activate(
        category: Category,
    ) -> Category:
        """Activate the category."""

        return CategoryService._set_active(
            category=category,
            is_active=True,
        )

    @staticmethod
    @transaction.atomic
    def deactivate(
        category: Category,
    ) -> Category:
        """Deactivate the category."""

        return CategoryService._set_active(
            category=category,
            is_active=False,
        )

    @staticmethod
    @transaction.atomic
    def delete(
        category: Category,
    ) -> None:
        """Delete the category."""

        category.delete()

    @staticmethod
    def _set_active(
        *,
        category: Category,
        is_active: bool,
    ) -> Category:
        """Update category active status."""

        category.is_active = is_active

        category.save(
            update_fields=[
                "is_active",
            ],
        )

        return category
