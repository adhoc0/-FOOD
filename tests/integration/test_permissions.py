"""Kullanıcı ve yönetim uçları için yetkilendirme testleri."""

from django.conf import settings
from django.test import Client
from django.urls import reverse


def test_anonymous_user_cannot_add_comment() -> None:
    response = Client().post(
        reverse("interactions:add_comment", kwargs={"recipe_id": 1}),
        {"content": "Yetkisiz yorum"},
    )

    assert response.status_code == 302
    assert "/hesap/login/" in response["Location"]


def test_anonymous_user_cannot_toggle_favorite() -> None:
    response = Client().post(
        reverse("interactions:toggle_favorite", kwargs={"recipe_id": 1}),
    )

    assert response.status_code == 302
    assert "/hesap/login/" in response["Location"]


def test_anonymous_user_cannot_open_admin() -> None:
    response = Client().get(f"/{settings.ADMIN_URL}")

    assert response.status_code == 302
    assert "login" in response["Location"]
