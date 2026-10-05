"""RFC 6238 TOTP (SHA-1, 6 hane, 30 sn) — harici bağımlılık olmadan.

Google Authenticator, Authy, 1Password vb. uygulamalarla uyumludur.
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import secrets
import struct
import time
from urllib.parse import quote

PERIOD_SECONDS = 30
DIGITS = 6
ALLOWED_DRIFT_STEPS = 1  # ±30 sn saat sapması


def generate_secret() -> str:
    """160 bitlik rastgele, base32 kodlu gizli anahtar üretir."""

    return base64.b32encode(secrets.token_bytes(20)).decode("ascii")


def current_step(now: float | None = None) -> int:
    return int((time.time() if now is None else now) // PERIOD_SECONDS)


def code_for_step(secret: str, step: int, digits: int = DIGITS) -> str:
    key = base64.b32decode(secret, casefold=True)
    digest = hmac.new(key, struct.pack(">Q", step), hashlib.sha1).digest()
    offset = digest[-1] & 0x0F
    value = struct.unpack(">I", digest[offset : offset + 4])[0] & 0x7FFFFFFF
    return str(value % 10**digits).zfill(digits)


def match_step(
    secret: str,
    code: str,
    *,
    last_used_step: int = 0,
    now: float | None = None,
) -> int | None:
    """Kod geçerliyse eşleşen adımı, değilse None döndürür.

    `last_used_step` ve öncesi reddedilir; böylece aynı kod tekrar kullanılamaz.
    """

    candidate = code.strip().replace(" ", "")
    if len(candidate) != DIGITS or not candidate.isdigit():
        return None

    center = current_step(now)
    for step in range(center - ALLOWED_DRIFT_STEPS, center + ALLOWED_DRIFT_STEPS + 1):
        if step <= last_used_step:
            continue
        if hmac.compare_digest(code_for_step(secret, step), candidate):
            return step
    return None


def provisioning_uri(secret: str, account: str, issuer: str) -> str:
    """Authenticator uygulamalarının okuduğu otpauth:// adresi."""

    label = quote(f"{issuer}:{account}")
    return (
        f"otpauth://totp/{label}?secret={secret}&issuer={quote(issuer)}"
        f"&algorithm=SHA1&digits={DIGITS}&period={PERIOD_SECONDS}"
    )
