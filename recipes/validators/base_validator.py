"""
Base validator.

Tüm validator sınıfları tarafından kullanılan ortak doğrulama yardımcıları.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BaseValidator:
    """Base validation helpers."""

    @staticmethod
    def validate_required_string(
        value: str,
        field: str,
    ) -> str:
        """
        Metin alanı doğrulaması.

        Kontroller:

        - None kabul edilmez.
        - String olmayan tipler reddedilir.
        - Boş veya sadece boşluklardan oluşan değerler reddedilir.

        Dönen değer strip edilmiş metindir.
        """

        if value is None:
            raise ValidationError(
                _("%(field)s is required."),
                params={
                    "field": field,
                },
            )

        if not isinstance(
            value,
            str,
        ):
            raise ValidationError(
                _("%(field)s must be a string."),
                params={
                    "field": field,
                },
            )

        value = value.strip()

        if not value:
            raise ValidationError(
                _("%(field)s cannot be empty."),
                params={
                    "field": field,
                },
            )

        return value

    @staticmethod
    def validate_length(
        value: str,
        field: str,
        minimum: int,
        maximum: int,
    ) -> None:
        """
        Metin uzunluğu doğrulaması.
        """

        length = len(value)

        if length < minimum:
            raise ValidationError(
                _("%(field)s must contain at least %(min)d characters."),
                params={
                    "field": field,
                    "min": minimum,
                },
            )

        if length > maximum:
            raise ValidationError(
                _("%(field)s cannot exceed %(max)d characters."),
                params={
                    "field": field,
                    "max": maximum,
                },
            )

    @staticmethod
    def validate_positive_integer(
        value: int,
        field: str,
        minimum: int,
        maximum: int,
    ) -> None:
        """
        Pozitif tam sayı doğrulaması.
        """

        if not isinstance(
            value,
            int,
        ):
            raise ValidationError(
                _("%(field)s must be an integer."),
                params={
                    "field": field,
                },
            )

        if value < minimum:
            raise ValidationError(
                _("%(field)s must be at least %(min)d."),
                params={
                    "field": field,
                    "min": minimum,
                },
            )

        if value > maximum:
            raise ValidationError(
                _("%(field)s cannot exceed %(max)d."),
                params={
                    "field": field,
                    "max": maximum,
                },
            )

    @staticmethod
    def validate_decimal(
        value: Decimal | int | float | str,
        field: str,
        minimum: Decimal,
        maximum: Decimal,
    ) -> Decimal:
        """
        Decimal doğrulaması.

        Dönen değer Decimal tipindedir.
        """

        try:
            value = Decimal(str(value))
        except (
            InvalidOperation,
            TypeError,
            ValueError,
        ) as exc:
            raise ValidationError(
                _("%(field)s is invalid."),
                params={
                    "field": field,
                },
            ) from exc

        if value.is_nan():
            raise ValidationError(
                _("%(field)s cannot be NaN."),
                params={
                    "field": field,
                },
            )

        if value.is_infinite():
            raise ValidationError(
                _("%(field)s cannot be infinite."),
                params={
                    "field": field,
                },
            )

        if value < minimum:
            raise ValidationError(
                _("%(field)s must be at least %(min)s."),
                params={
                    "field": field,
                    "min": minimum,
                },
            )

        if value > maximum:
            raise ValidationError(
                _("%(field)s cannot exceed %(max)s."),
                params={
                    "field": field,
                    "max": maximum,
                },
            )

        return value
