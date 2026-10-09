"""ContactValidator testleri."""

import pytest
from django.core.exceptions import ValidationError

from pages.validators.contact_validator import ContactValidator
from recipes.constants import (
    MAX_CONTACT_MESSAGE_LENGTH,
    MAX_CONTACT_NAME_LENGTH,
    MAX_CONTACT_SUBJECT_LENGTH,
    MIN_CONTACT_MESSAGE_LENGTH,
    MIN_CONTACT_NAME_LENGTH,
    MIN_CONTACT_SUBJECT_LENGTH,
)

VALID = {
    "name": "Ayşe Yılmaz",
    "email": "ayse@example.com",
    "subject": "Tarif önerisi",
    "message": "Merhaba, yöremize ait bir tarifi paylaşmak istiyorum.",
}


@pytest.mark.parametrize(
    ("method", "min_len", "max_len"),
    [
        ("validate_name", MIN_CONTACT_NAME_LENGTH, MAX_CONTACT_NAME_LENGTH),
        ("validate_subject", MIN_CONTACT_SUBJECT_LENGTH, MAX_CONTACT_SUBJECT_LENGTH),
        ("validate_message", MIN_CONTACT_MESSAGE_LENGTH, MAX_CONTACT_MESSAGE_LENGTH),
    ],
)
class TestLengthRules:
    def test_too_short(self, method, min_len, max_len):
        with pytest.raises(ValidationError):
            getattr(ContactValidator, method)("a" * (min_len - 1))

    def test_too_long(self, method, min_len, max_len):
        with pytest.raises(ValidationError):
            getattr(ContactValidator, method)("a" * (max_len + 1))

    def test_boundaries_accepted(self, method, min_len, max_len):
        getattr(ContactValidator, method)("a" * min_len)
        getattr(ContactValidator, method)("a" * max_len)

    def test_surrounding_whitespace_is_ignored(self, method, min_len, max_len):
        with pytest.raises(ValidationError):
            getattr(ContactValidator, method)("  " + "a" * (min_len - 1) + "  ")


class TestEmail:
    def test_invalid_email(self):
        with pytest.raises(ValidationError):
            ContactValidator.validate_email("gecersiz")

    def test_valid_email_with_spaces(self):
        ContactValidator.validate_email("  ayse@example.com ")


class TestContactData:
    def test_valid_data(self):
        ContactValidator.validate_contact_data(VALID)

    @pytest.mark.parametrize("field", list(VALID))
    def test_each_invalid_field_is_rejected(self, field):
        data = {**VALID, field: "x"}

        with pytest.raises(ValidationError):
            ContactValidator.validate_contact_data(data)

    def test_missing_fields_are_skipped(self):
        ContactValidator.validate_contact_data({})
