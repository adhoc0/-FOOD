"""Kullanıcı adı bazlı giriş denemesi sınırı (brute-force koruması).

IP bazlı hız sınırı `common.middleware.WriteRateLimitMiddleware` içindedir; bu
modül dağıtık (çok IP'li) denemelere karşı aynı hesabı hedef alan başarısız
girişleri sayar. Sayaç cache'te tutulur (Redis ile tüm worker'lar arasında
paylaşılır). Kullanıcı adı var olsun ya da olmasın aynı sayaç işler; böylece
hesap varlığı sızdırılmaz.
"""

from __future__ import annotations

import hashlib

from django.core.cache import cache

MAX_FAILED_ATTEMPTS = 5
LOCKOUT_SECONDS = 15 * 60


def _key(username: str) -> str:
    digest = hashlib.sha256(username.strip().lower().encode("utf-8")).hexdigest()
    return f"login-failures:{digest}"


def is_locked(username: str) -> bool:
    """Kullanıcı adı için deneme hakkı bittiyse True döner."""

    return cache.get(_key(username), 0) >= MAX_FAILED_ATTEMPTS


def register_failure(username: str) -> int:
    """Başarısız denemeyi sayar ve güncel sayıyı döndürür."""

    key = _key(username)

    if cache.add(key, 1, timeout=LOCKOUT_SECONDS):
        return 1

    try:
        return cache.incr(key)
    except ValueError:
        cache.set(key, 1, timeout=LOCKOUT_SECONDS)
        return 1


def reset(username: str) -> None:
    """Başarılı girişten sonra sayacı sıfırlar."""

    cache.delete(_key(username))
