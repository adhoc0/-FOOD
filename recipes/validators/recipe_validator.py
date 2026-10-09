"""
Recipe business validations.

Tarif verilerinin iş kurallarına uygunluğunu doğrular.
View, Form veya Model katmanında doğrulama yapılmaz.
Tüm iş kuralları bu sınıfta toplanır.
"""

from __future__ import annotations

from typing import Any

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from recipes.choices import Status
from recipes.constants import (
    MAX_INSTRUCTIONS_LENGTH,
    MAX_SERVINGS,
    MAX_SUMMARY_LENGTH,
    MAX_TIME_MINUTES,
    MAX_TITLE_LENGTH,
    MIN_INSTRUCTIONS_LENGTH,
    MIN_SERVINGS,
    MIN_SUMMARY_LENGTH,
    MIN_TIME_MINUTES,
    MIN_TITLE_LENGTH,
)
from recipes.validators.base_validator import BaseValidator


class RecipeValidator(BaseValidator):
    """Recipe business validations."""

    ALLOWED_TRANSITIONS: dict[str, frozenset[str]] = {
        Status.DRAFT: frozenset(
            {
                Status.PUBLISHED,
            },
        ),
        Status.PUBLISHED: frozenset(
            {
                Status.DRAFT,
                Status.ARCHIVED,
            },
        ),
        Status.ARCHIVED: frozenset(
            {
                Status.DRAFT,
            },
        ),
    }

    @classmethod
    def validate_title(
        cls,
        value: str,
    ) -> None:
        """Tarif başlığını doğrular."""

        value = cls.validate_required_string(
            value,
            "Recipe title",
        )

        cls.validate_length(
            value=value,
            field="Recipe title",
            minimum=MIN_TITLE_LENGTH,
            maximum=MAX_TITLE_LENGTH,
        )

    @classmethod
    def validate_summary(
        cls,
        value: str,
    ) -> None:
        """Tarif özetini doğrular."""

        value = cls.validate_required_string(
            value,
            "Recipe summary",
        )

        cls.validate_length(
            value=value,
            field="Recipe summary",
            minimum=MIN_SUMMARY_LENGTH,
            maximum=MAX_SUMMARY_LENGTH,
        )

    @classmethod
    def validate_instructions(
        cls,
        value: str,
    ) -> None:
        """Hazırlanış metnini doğrular."""

        value = cls.validate_required_string(
            value,
            "Recipe instructions",
        )

        cls.validate_length(
            value=value,
            field="Recipe instructions",
            minimum=MIN_INSTRUCTIONS_LENGTH,
            maximum=MAX_INSTRUCTIONS_LENGTH,
        )

    @classmethod
    def validate_preparation_time(
        cls,
        value: int,
    ) -> None:
        """Hazırlık süresini doğrular."""

        cls.validate_positive_integer(
            value=value,
            field="Preparation time",
            minimum=MIN_TIME_MINUTES,
            maximum=MAX_TIME_MINUTES,
        )

    @classmethod
    def validate_cooking_time(
        cls,
        value: int,
    ) -> None:
        """Pişirme süresini doğrular."""

        cls.validate_positive_integer(
            value=value,
            field="Cooking time",
            minimum=MIN_TIME_MINUTES,
            maximum=MAX_TIME_MINUTES,
        )

    @classmethod
    def validate_servings(
        cls,
        value: int,
    ) -> None:
        """Porsiyon sayısını doğrular."""

        cls.validate_positive_integer(
            value=value,
            field="Servings",
            minimum=MIN_SERVINGS,
            maximum=MAX_SERVINGS,
        )

    @staticmethod
    def validate_status(
        value: str,
    ) -> None:
        """Tarif durumunu doğrular."""

        if value not in {
            Status.DRAFT,
            Status.PUBLISHED,
            Status.ARCHIVED,
        }:
            raise ValidationError(
                _("Invalid recipe status."),
            )

    @classmethod
    def validate_status_transition(
        cls,
        current_status: str,
        target_status: str,
    ) -> None:
        """Durum geçişlerini doğrular."""

        if current_status == target_status:
            return

        allowed = cls.ALLOWED_TRANSITIONS.get(
            current_status,
            frozenset(),
        )

        if target_status not in allowed:
            raise ValidationError(
                _("Status transition is not allowed."),
            )

    @classmethod
    def validate_recipe_data(
        cls,
        data: dict[str, Any],
    ) -> None:
        """Tarif verilerini tek seferde doğrular."""

        if "title" in data:
            cls.validate_title(data["title"])

        if "summary" in data:
            cls.validate_summary(data["summary"])

        if "instructions" in data:
            cls.validate_instructions(data["instructions"])

        if "preparation_time" in data:
            cls.validate_preparation_time(data["preparation_time"])

        if "cooking_time" in data:
            cls.validate_cooking_time(data["cooking_time"])

        if "servings" in data:
            cls.validate_servings(data["servings"])

        if "status" in data:
            cls.validate_status(data["status"])

        if (
            "preparation_time" in data
            and "cooking_time" in data
        ):
            total_time = (
                data["preparation_time"]
                + data["cooking_time"]
            )

            if total_time > 1440:
                raise ValidationError(
                    _("Total recipe time cannot exceed 24 hours."),
                )
