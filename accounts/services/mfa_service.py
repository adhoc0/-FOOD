"""Yönetici hesapları için iki adımlı doğrulama akışı."""

from __future__ import annotations

from django.conf import settings
from django.http import HttpRequest

from accounts.models import CustomUser, TOTPDevice
from accounts.services import login_throttle, totp

SESSION_KEY = "mfa_verified"
ISSUER = "Türkiye Yöresel Yemekleri"


def requires_mfa(user: object) -> bool:
    """Bu kullanıcı için 2FA zorunlu mu? (şimdilik yalnızca personel)"""

    return bool(
        getattr(settings, "MFA_REQUIRED_FOR_STAFF", True)
        and getattr(user, "is_authenticated", False)
        and getattr(user, "is_staff", False)
    )


def is_verified(request: HttpRequest) -> bool:
    return bool(request.session.get(SESSION_KEY))


def mark_verified(request: HttpRequest) -> None:
    request.session[SESSION_KEY] = True


def has_confirmed_device(user: CustomUser) -> bool:
    return TOTPDevice.objects.filter(user=user, confirmed=True).exists()


def get_or_create_pending_device(user: CustomUser) -> TOTPDevice:
    device, _ = TOTPDevice.objects.get_or_create(
        user=user,
        defaults={"secret": totp.generate_secret()},
    )
    return device


def provisioning_uri(device: TOTPDevice, user: CustomUser) -> str:
    return totp.provisioning_uri(device.secret, user.email or user.get_username(), ISSUER)


def _throttle_key(user: CustomUser) -> str:
    return f"mfa:{user.pk}"


def verify_code(user: CustomUser, code: str, *, confirm: bool = False) -> bool:
    """Kodu doğrular. Başarısız denemeler hesap bazında sınırlanır."""

    key = _throttle_key(user)
    if login_throttle.is_locked(key):
        return False

    device = TOTPDevice.objects.filter(user=user).first()
    step = (
        totp.match_step(device.secret, code, last_used_step=device.last_used_step)
        if device
        else None
    )
    if device is None or step is None:
        login_throttle.register_failure(key)
        return False

    device.last_used_step = step
    if confirm:
        device.confirmed = True
    device.save(update_fields=["last_used_step", "confirmed"])
    login_throttle.reset(key)
    return True


def is_locked(user: CustomUser) -> bool:
    return login_throttle.is_locked(_throttle_key(user))
