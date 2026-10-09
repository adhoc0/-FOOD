"""accounts.services.user_service testleri."""

import pytest
from django.contrib.auth import get_user_model

from accounts.services import (
    activate_user,
    create_user,
    deactivate_user,
    update_user,
)
from tests.factories import UserFactory

User = get_user_model()


@pytest.mark.django_db
class TestUserService:
    def test_create_user_hashes_password(self):
        user = create_user(
            username="yeni",
            email="yeni@example.com",
            password="Guvenli-Sifre-123",
        )

        assert user.pk is not None
        assert user.password != "Guvenli-Sifre-123"
        assert user.check_password("Guvenli-Sifre-123")

    def test_update_user_changes_fields_and_password(self):
        user = UserFactory()

        updated = update_user(
            user,
            first_name="Ayşe",
            password="Baska-Sifre-456",
        )

        updated.refresh_from_db()
        assert updated.first_name == "Ayşe"
        assert updated.check_password("Baska-Sifre-456")

    def test_update_user_without_password_keeps_it(self):
        user = UserFactory()
        old_hash = user.password

        update_user(user, first_name="Mehmet")

        user.refresh_from_db()
        assert user.password == old_hash

    def test_deactivate_and_activate(self):
        user = UserFactory()

        deactivate_user(user)
        user.refresh_from_db()
        assert user.is_active is False

        activate_user(user)
        user.refresh_from_db()
        assert user.is_active is True
