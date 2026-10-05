from __future__ import annotations

import pytest
from django.conf import settings
from django.core.cache import cache
from django.test import Client, override_settings
from django.urls import reverse

from accounts.models import CustomUser, TOTPDevice
from accounts.services import totp

pytestmark = pytest.mark.django_db

ADMIN = f"/{settings.ADMIN_URL}"


@pytest.fixture(autouse=True)
def _clear_cache() -> None:
    cache.clear()


@pytest.fixture
def staff() -> CustomUser:
    return CustomUser.objects.create_user(
        username="staffer",
        email="staff@example.com",
        password="pw-12345-xyz",
        is_staff=True,
        is_superuser=True,
    )


def _code(secret: str) -> str:
    return totp.code_for_step(secret, totp.current_step())


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_staff_without_device_is_sent_to_setup(staff: CustomUser) -> None:
    client = Client()
    client.force_login(staff)
    response = client.get(ADMIN)
    assert response.status_code == 302
    assert response["Location"].startswith(reverse("accounts:mfa_setup"))


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_setup_confirms_device_and_unlocks_admin(staff: CustomUser) -> None:
    client = Client()
    client.force_login(staff)
    page = client.get(reverse("accounts:mfa_setup"))
    assert page.status_code == 200
    secret = TOTPDevice.objects.get(user=staff).secret
    assert secret in page.content.decode()

    response = client.post(reverse("accounts:mfa_setup"), {"code": _code(secret)})
    assert response.status_code == 302
    assert TOTPDevice.objects.get(user=staff).confirmed is True
    assert client.get(ADMIN).status_code == 200


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_wrong_code_does_not_confirm_or_unlock(staff: CustomUser) -> None:
    client = Client()
    client.force_login(staff)
    client.get(reverse("accounts:mfa_setup"))
    response = client.post(reverse("accounts:mfa_setup"), {"code": "000000"})
    assert response.status_code == 200
    assert TOTPDevice.objects.get(user=staff).confirmed is False
    assert client.get(ADMIN).status_code == 302


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_verify_flow_for_existing_device(staff: CustomUser) -> None:
    secret = totp.generate_secret()
    TOTPDevice.objects.create(user=staff, secret=secret, confirmed=True)
    client = Client()
    client.force_login(staff)

    redirect = client.get(ADMIN)
    assert redirect["Location"].startswith(reverse("accounts:mfa_verify"))

    ok = client.post(f"{reverse('accounts:mfa_verify')}?next={ADMIN}", {"code": _code(secret)})
    assert ok.status_code == 302
    assert ok["Location"] == ADMIN
    assert client.get(ADMIN).status_code == 200


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_code_cannot_be_replayed(staff: CustomUser) -> None:
    secret = totp.generate_secret()
    TOTPDevice.objects.create(user=staff, secret=secret, confirmed=True)
    code = _code(secret)

    first = Client()
    first.force_login(staff)
    assert first.post(reverse("accounts:mfa_verify"), {"code": code}).status_code == 302

    second = Client()
    second.force_login(staff)
    assert second.post(reverse("accounts:mfa_verify"), {"code": code}).status_code == 200
    assert second.get(ADMIN).status_code == 302


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_verify_locks_after_repeated_failures(staff: CustomUser) -> None:
    secret = totp.generate_secret()
    TOTPDevice.objects.create(user=staff, secret=secret, confirmed=True)
    client = Client()
    client.force_login(staff)
    for _ in range(5):
        client.post(reverse("accounts:mfa_verify"), {"code": "000000"})

    response = client.post(reverse("accounts:mfa_verify"), {"code": _code(secret)})
    assert response.status_code == 200
    assert "15 dakika" in response.content.decode()
    assert client.get(ADMIN).status_code == 302


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_next_open_redirect_is_ignored(staff: CustomUser) -> None:
    secret = totp.generate_secret()
    TOTPDevice.objects.create(user=staff, secret=secret, confirmed=True)
    client = Client()
    client.force_login(staff)
    response = client.post(
        f"{reverse('accounts:mfa_verify')}?next=https://evil.example/", {"code": _code(secret)}
    )
    assert response["Location"] == reverse("accounts:profile")


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_regular_user_is_not_affected() -> None:
    user = CustomUser.objects.create_user(
        username="u", email="u@example.com", password="pw-12345-xyz"
    )
    client = Client()
    client.force_login(user)
    assert client.get(reverse("accounts:profile")).status_code == 200


@override_settings(MFA_REQUIRED_FOR_STAFF=True)
def test_setup_redirects_when_already_enabled(staff: CustomUser) -> None:
    TOTPDevice.objects.create(user=staff, secret=totp.generate_secret(), confirmed=True)
    client = Client()
    client.force_login(staff)
    response = client.get(reverse("accounts:mfa_setup"))
    assert response.status_code == 302
    assert response["Location"].startswith(reverse("accounts:mfa_verify"))


def test_anonymous_is_sent_to_login() -> None:
    assert Client().get(reverse("accounts:mfa_verify")).status_code == 302

