"""accounts.validators.user_validator testleri."""

import pytest
from django.core.exceptions import ValidationError

from accounts.validators.user_validator import (
    validate_unique_email,
    validate_username,
)
from tests.factories import UserFactory


@pytest.mark.django_db
class TestUserValidators:
    def test_unique_email_rejects_existing_case_insensitive(self):
        UserFactory(email="kayitli@example.com")

        with pytest.raises(ValidationError):
            validate_unique_email("KAYITLI@example.com")

    def test_unique_email_accepts_new(self):
        validate_unique_email("yeni@example.com")

    def test_username_too_short(self):
        with pytest.raises(ValidationError):
            validate_username("ab")

    def test_username_valid(self):
        validate_username("abc")
