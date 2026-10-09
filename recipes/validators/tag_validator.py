"""
Tag business validations.

Etiket verilerinin iş kurallarına uygunluğunu doğrular.
View, Form veya Model içerisinde iş kuralı bulunmaz.
Tüm doğrulamalar bu sınıf üzerinden gerçekleştirilir.
"""

from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    MAX_TAG_DESCRIPTION_LENGTH,
    MAX_TAG_NAME_LENGTH,
    MIN_TAG_NAME_LENGTH,
)
from recipes.validators.base_validator import BaseValidator


class TagValidator(BaseValidator):
    """Business validations for Tag."""

    @classmethod
    def validate_name(
        cls,
        value: str,
    ) -> None:
        """
        Etiket adını doğrular.

        Kontroller:

        - Zorunlu alan
        - Minimum uzunluk
        - Maksimum uzunluk
        """

        value = cls.validate_required_string(
            value,
            "Tag name",
        )

        cls.validate_length(
            value=value,
            field="Tag name",
            minimum=MIN_TAG_NAME_LENGTH,
            maximum=MAX_TAG_NAME_LENGTH,
        )

    @classmethod
    def validate_description(
        cls,
        value: str,
    ) -> None:
        """
        Etiket açıklamasını doğrular.

        Açıklama zorunlu değildir.
        Girilmişse yalnızca maksimum uzunluk kontrol edilir.
        """

        if not value:
            return

        value = value.strip()

        if len(value) > MAX_TAG_DESCRIPTION_LENGTH:
            raise ValidationError(
                _(
                    "Tag description cannot exceed %(max)d characters."
                ),
                params={
                    "max": MAX_TAG_DESCRIPTION_LENGTH,
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
                _("Tag active status must be a boolean."),
            )

    @classmethod
    def validate_tag_data(
        cls,
        data: dict[str, Any],
    ) -> None:
        """
        Etiket oluşturma veya güncelleme
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
