"""Giriş, çıkış ve şifre sıfırlama akışı entegrasyon testleri."""

import re

import pytest
from django.core import mail
from django.core.cache import cache
from django.test import Client
from django.urls import reverse

from tests.factories import UserFactory

VALID_PASSWORD = "Gecerli-Sifre-2026!"
NEW_PASSWORD = "Yeni-Sifre-2026-Guvenli!"


@pytest.fixture(autouse=True)
def clear_rate_limit_cache():
    cache.clear()
    yield
    cache.clear()


def _create_user_with_password():
    user = UserFactory()
    user.set_password(VALID_PASSWORD)
    user.save()
    return user


@pytest.mark.django_db
class TestLoginLogout:
    def test_successful_login_redirects_to_profile(self):
        user = _create_user_with_password()

        response = Client().post(
            reverse("accounts:login"),
            {"username": user.username, "password": VALID_PASSWORD},
        )

        assert response.status_code == 302
        assert response["Location"] == reverse("accounts:profile")

    def test_logout_redirects_to_home(self):
        client = Client()
        client.force_login(_create_user_with_password())

        response = client.post(reverse("accounts:logout"))

        assert response.status_code == 302
        assert response["Location"] == reverse("pages:home")

    def test_login_page_links_to_password_reset(self):
        response = Client().get(reverse("accounts:login"))

        assert reverse("accounts:password_reset").encode() in response.content


@pytest.mark.django_db
class TestPasswordReset:
    def test_reset_form_renders(self):
        response = Client().get(reverse("accounts:password_reset"))

        assert response.status_code == 200

    def test_reset_request_sends_email_with_namespaced_confirm_link(self):
        user = _create_user_with_password()

        response = Client().post(
            reverse("accounts:password_reset"),
            {"email": user.email},
        )

        assert response.status_code == 302
        assert response["Location"] == reverse("accounts:password_reset_done")
        assert len(mail.outbox) == 1
        assert user.email in mail.outbox[0].to
        assert re.search(r"/hesap/password-reset/[^/\s]+/[^/\s]+/", mail.outbox[0].body)

    def test_unknown_email_does_not_reveal_account_existence(self):
        response = Client().post(
            reverse("accounts:password_reset"),
            {"email": "kayitli-degil@example.com"},
        )

        assert response.status_code == 302
        assert response["Location"] == reverse("accounts:password_reset_done")
        assert mail.outbox == []

    def test_full_reset_flow_changes_password(self):
        user = _create_user_with_password()
        client = Client()
        client.post(reverse("accounts:password_reset"), {"email": user.email})
        confirm_path = re.search(
            r"/hesap/password-reset/[^/\s]+/[^/\s]+/",
            mail.outbox[0].body,
        ).group(0)

        confirm_page = client.get(confirm_path, follow=True)
        set_password_url = confirm_page.redirect_chain[-1][0]
        response = client.post(
            set_password_url,
            {"new_password1": NEW_PASSWORD, "new_password2": NEW_PASSWORD},
        )

        assert response.status_code == 302
        assert response["Location"] == reverse("accounts:password_reset_complete")
        user.refresh_from_db()
        assert user.check_password(NEW_PASSWORD)

    def test_invalid_token_shows_error_message(self):
        response = Client().get(
            reverse(
                "accounts:password_reset_confirm",
                kwargs={"uidb64": "abc", "token": "invalid-token"},
            ),
        )

        assert response.status_code == 200
        assert "geçersiz" in response.content.decode()


@pytest.mark.django_db
class TestLoginBruteForceProtection:
    def _attempt(self, client, username, password):
        return client.post(
            reverse("accounts:login"),
            {"username": username, "password": password},
        )

    def test_account_is_locked_after_repeated_failures(self):
        from accounts.services.login_throttle import MAX_FAILED_ATTEMPTS

        user = _create_user_with_password()

        for index in range(MAX_FAILED_ATTEMPTS):
            # Farklı istemciler: IP bazlı sınır değil hesap bazlı kilit test edilir.
            response = self._attempt(Client(REMOTE_ADDR=f"10.0.0.{index}"), user.username, "yanlis")
            assert response.status_code == 200

        # Doğru parola bile kilit süresince reddedilir.
        response = self._attempt(Client(REMOTE_ADDR="10.0.1.1"), user.username, VALID_PASSWORD)

        assert response.status_code == 200
        assert "Çok fazla başarısız giriş denemesi" in response.content.decode()
        assert "_auth_user_id" not in response.wsgi_request.session

    def test_successful_login_resets_counter(self):
        user = _create_user_with_password()

        for _ in range(2):
            self._attempt(Client(), user.username, "yanlis")
        ok = self._attempt(Client(), user.username, VALID_PASSWORD)
        assert ok.status_code == 302

        for _ in range(2):
            self._attempt(Client(), user.username, "yanlis")
        ok_again = self._attempt(Client(), user.username, VALID_PASSWORD)
        assert ok_again.status_code == 302

    def test_unknown_username_is_throttled_with_same_message(self):
        from accounts.services.login_throttle import MAX_FAILED_ATTEMPTS

        for index in range(MAX_FAILED_ATTEMPTS):
            self._attempt(Client(REMOTE_ADDR=f"10.0.2.{index}"), "yok-boyle-biri", "x")

        response = self._attempt(Client(REMOTE_ADDR="10.0.3.1"), "yok-boyle-biri", "x")

        assert "Çok fazla başarısız giriş denemesi" in response.content.decode()
