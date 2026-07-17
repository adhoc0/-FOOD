"""
Contact form validations.

İletişim formu verilerinin doğruluğunu sağlar.
"""

from __future__ import annotations

from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email
from django.utils.translation import gettext_lazy as _

from recipes.constants import (
    MAX_CONTACT_MESSAGE_LENGTH,
    MAX_CONTACT_NAME_LENGTH,
    MAX_CONTACT_SUBJECT_LENGTH,
    MIN_CONTACT_MESSAGE_LENGTH,
    MIN_CONTACT_NAME_LENGTH,
    MIN_CONTACT_SUBJECT_LENGTH,
)


class ContactValidator:
    """Contact form validations."""

    @staticmethod
    def validate_name(value: str) -> None:
        """İsim doğrulaması."""
        stripped = value.strip()

        if len(stripped) < MIN_CONTACT_NAME_LENGTH:
            raise ValidationError(
                _("İsim en az %(min)d karakter olmalıdır."),
                params={"min": MIN_CONTACT_NAME_LENGTH},
            )

        if len(stripped) > MAX_CONTACT_NAME_LENGTH:
            raise ValidationError(
                _("İsim en fazla %(max)d karakter olabilir."),
                params={"max": MAX_CONTACT_NAME_LENGTH},
            )

    @staticmethod
    def validate_email(value: str) -> None:
        """E-posta doğrulaması."""
        django_validate_email(value.strip())

    @staticmethod
    def validate_subject(value: str) -> None:
        """Konu doğrulaması."""
        stripped = value.strip()

        if len(stripped) < MIN_CONTACT_SUBJECT_LENGTH:
            raise ValidationError(
                _("Konu en az %(min)d karakter olmalıdır."),
                params={"min": MIN_CONTACT_SUBJECT_LENGTH},
            )

        if len(stripped) > MAX_CONTACT_SUBJECT_LENGTH:
            raise ValidationError(
                _("Konu en fazla %(max)d karakter olabilir."),
                params={"max": MAX_CONTACT_SUBJECT_LENGTH},
            )

    @staticmethod
    def validate_message(value: str) -> None:
        """Mesaj doğrulaması."""
        stripped = value.strip()

        if len(stripped) < MIN_CONTACT_MESSAGE_LENGTH:
            raise ValidationError(
                _("Mesaj en az %(min)d karakter olmalıdır."),
                params={"min": MIN_CONTACT_MESSAGE_LENGTH},
            )

        if len(stripped) > MAX_CONTACT_MESSAGE_LENGTH:
            raise ValidationError(
                _("Mesaj en fazla %(max)d karakter olabilir."),
                params={"max": MAX_CONTACT_MESSAGE_LENGTH},
            )

    @classmethod
    def validate_contact_data(cls, data: dict) -> None:
        """Tüm iletişim formu alanlarını toplu doğrular."""
        if "name" in data:
            cls.validate_name(data["name"])

        if "email" in data:
            cls.validate_email(data["email"])

        if "subject" in data:
            cls.validate_subject(data["subject"])

        if "message" in data:
            cls.validate_message(data["message"])
