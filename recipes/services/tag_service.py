from __future__ import annotations

from typing import Any

from django.db import transaction

from recipes.models.tag import Tag


class TagService:
    """Service layer responsible for Tag write operations."""

    @staticmethod
    @transaction.atomic
    def create(**data: Any) -> Tag:
        """Create a new tag."""

        instance: Tag = Tag.objects.create(**data)

        return instance

    @staticmethod
    @transaction.atomic
    def update(
        tag: Tag,
        **data: Any,
    ) -> Tag:
        """Update tag fields."""

        if not data:
            return tag

        update_fields: list[str] = []

        for field, value in data.items():
            setattr(tag, field, value)
            update_fields.append(field)

        tag.save(update_fields=update_fields)

        return tag

    @staticmethod
    @transaction.atomic
    def activate(
        tag: Tag,
    ) -> Tag:
        """Activate the tag."""

        return TagService._set_active(
            tag=tag,
            is_active=True,
        )

    @staticmethod
    @transaction.atomic
    def deactivate(
        tag: Tag,
    ) -> Tag:
        """Deactivate the tag."""

        return TagService._set_active(
            tag=tag,
            is_active=False,
        )

    @staticmethod
    @transaction.atomic
    def delete(
        tag: Tag,
    ) -> None:
        """Delete the tag."""

        tag.delete()

    @staticmethod
    def _set_active(
        *,
        tag: Tag,
        is_active: bool,
    ) -> Tag:
        """Update tag active status."""

        tag.is_active = is_active

        tag.save(
            update_fields=[
                "is_active",
            ],
        )

        return tag
