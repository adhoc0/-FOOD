"""
Category business validations.

Kategori verilerinin iş kurallarına uygunluğunu doğrular.
View, Form veya Model içerisinde iş kuralı bulunmaz.
Tüm doğrulamalar bu sınıf üzerinden gerçekleştirilir.
"""

from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    MAX_CATEGORY_DESCRIPTION_LENGTH,
    MAX_CATEGORY_NAME_LENGTH,
    MIN_CATEGORY_NAME_LENGTH,
)

from .base_validator import BaseValidator


class CategoryValidator(BaseValidator):
    """Business validations for Category."""

    @classmethod
    def validate_name(
        cls,
        value: str,
    ) -> None:
        """
        Kategori adını doğrular.

        Kontroller:

        - Zorunlu alan
        - Minimum uzunluk
        - Maksimum uzunluk
        """

        value = cls.validate_required_string(
            value,
            "Category name",
        )

        cls.validate_length(
            value=value,
            field="Category name",
            minimum=MIN_CATEGORY_NAME_LENGTH,
            maximum=MAX_CATEGORY_NAME_LENGTH,
        )

    @classmethod
    def validate_description(
        cls,
        value: str,
    ) -> None:
        """
        Kategori açıklamasını doğrular.

        Açıklama zorunlu değildir.
        Girilmişse yalnızca maksimum uzunluk kontrol edilir.
        """

        if not value:
            return

        value = value.strip()

        if len(value) > MAX_CATEGORY_DESCRIPTION_LENGTH:
            raise ValidationError(
                _(
                    "Category description cannot exceed %(max)d characters."
                ),
                params={
                    "max": MAX_CATEGORY_DESCRIPTION_LENGTH,
            },
        )

    @classmethod
    def validate_category_data(
        cls,
        data: dict[str, Any],
    ) -> None:
        """
        Kategori oluşturma veya güncelleme
        verilerini tek seferde doğrular.
        """

        if "name" in data:
            cls.validate_name(
                data["name"],
            )

        if "description" in data:
            cls.validate_description(
                data["description"],
            )

    @staticmethod
    def validate_is_active(
        value: bool,
    ) -> None:
        """
        is_active alanının bool olduğunu doğrular.
        """

        if not isinstance(
            value,
            bool,
        ):
            raise ValidationError(
                _("Category active status must be a boolean."),
            )
