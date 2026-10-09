"""CategoryValidator testleri."""

import pytest
from django.core.exceptions import ValidationError

from recipes.constants import (
    MAX_CATEGORY_DESCRIPTION_LENGTH,
    MAX_CATEGORY_NAME_LENGTH,
    MIN_CATEGORY_NAME_LENGTH,
)
from recipes.validators.category_validator import CategoryValidator


class TestCategoryValidatorName:
    def test_accepts_name_within_bounds(self):
        CategoryValidator.validate_name("Çorbalar")

    def test_accepts_minimum_and_maximum_length(self):
        CategoryValidator.validate_name("a" * MIN_CATEGORY_NAME_LENGTH)
        CategoryValidator.validate_name("a" * MAX_CATEGORY_NAME_LENGTH)

    @pytest.mark.parametrize("value", [None, "", "   ", 123])
    def test_rejects_missing_blank_or_non_string(self, value):
        with pytest.raises(ValidationError):
            CategoryValidator.validate_name(value)

    def test_rejects_too_short_and_too_long(self):
        with pytest.raises(ValidationError):
            CategoryValidator.validate_name("a" * (MIN_CATEGORY_NAME_LENGTH - 1))
        with pytest.raises(ValidationError):
            CategoryValidator.validate_name("a" * (MAX_CATEGORY_NAME_LENGTH + 1))


class TestCategoryValidatorDescription:
    @pytest.mark.parametrize("value", [None, ""])
    def test_description_is_optional(self, value):
        CategoryValidator.validate_description(value)

    def test_accepts_description_at_the_limit(self):
        CategoryValidator.validate_description("a" * MAX_CATEGORY_DESCRIPTION_LENGTH)

    def test_rejects_description_over_the_limit(self):
        with pytest.raises(ValidationError):
            CategoryValidator.validate_description(
                "a" * (MAX_CATEGORY_DESCRIPTION_LENGTH + 1)
            )


class TestCategoryValidatorData:
    def test_validates_only_present_fields(self):
        CategoryValidator.validate_category_data({})
        CategoryValidator.validate_category_data({"name": "Tatlılar"})

    def test_invalid_name_in_payload_is_rejected(self):
        with pytest.raises(ValidationError):
            CategoryValidator.validate_category_data({"name": ""})

    def test_invalid_description_in_payload_is_rejected(self):
        with pytest.raises(ValidationError):
            CategoryValidator.validate_category_data(
                {"name": "Tatlılar", "description": "a" * 2000}
            )


class TestCategoryValidatorIsActive:
    @pytest.mark.parametrize("value", [True, False])
    def test_accepts_booleans(self, value):
        CategoryValidator.validate_is_active(value)

    @pytest.mark.parametrize("value", [1, "true", None])
    def test_rejects_non_booleans(self, value):
        with pytest.raises(ValidationError):
            CategoryValidator.validate_is_active(value)
