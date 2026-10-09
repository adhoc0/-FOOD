"""
Cuisine business validations.

Mutfak verilerinin iş kurallarına uygunluğunu doğrular.
View, Form veya Model içerisinde iş kuralı bulunmaz.
Tüm doğrulamalar bu sınıf üzerinden gerçekleştirilir.
"""

from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    MAX_CUISINE_DESCRIPTION_LENGTH,
    MAX_CUISINE_NAME_LENGTH,
    MIN_CUISINE_NAME_LENGTH,
)
from recipes.validators.base_validator import BaseValidator


class CuisineValidator(BaseValidator):
    """Business validations for Cuisine."""

    @classmethod
    def validate_name(
        cls,
        value: str,
    ) -> None:
        """
        Mutfak adını doğrular.

        Kontroller:

        - Zorunlu alan
        - Minimum uzunluk
        - Maksimum uzunluk
        """

        value = cls.validate_required_string(
            value,
            "Cuisine name",
        )

        cls.validate_length(
            value=value,
            field="Cuisine name",
            minimum=MIN_CUISINE_NAME_LENGTH,
            maximum=MAX_CUISINE_NAME_LENGTH,
        )

    @classmethod
    def validate_description(
        cls,
        value: str,
    ) -> None:
        """
        Mutfak açıklamasını doğrular.

        Açıklama zorunlu değildir.
        Girilmişse yalnızca maksimum uzunluk kontrol edilir.
        """

        if not value:
            return

        value = value.strip()

        if len(value) > MAX_CUISINE_DESCRIPTION_LENGTH:
            raise ValidationError(
                _(
                    "Cuisine description cannot exceed %(max)d characters."
                ),
                params={
                    "max": MAX_CUISINE_DESCRIPTION_LENGTH,
                },
            )

    @staticmethod
    def validate_is_active(
        value: bool,
    ) -> None:
        """
        is_active alanının bool tipinde olduğunu doğrular.
        """

        if not isinstance(
            value,
            bool,
        ):
            raise ValidationError(
                _("Cuisine active status must be a boolean."),
            )

    @classmethod
    def validate_cuisine_data(
        cls,
        data: dict[str, Any],
    ) -> None:
        """
        Mutfak oluşturma veya güncelleme
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

        if "is_active" in data:
            cls.validate_is_active(
                data["is_active"],
            )
