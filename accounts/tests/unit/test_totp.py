from __future__ import annotations

from accounts.services import totp

# RFC 6238 test anahtarı: ASCII "12345678901234567890"
RFC_SECRET = "GEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ"


def test_rfc6238_vector() -> None:
    # T=59 → adım 1; SHA-1, 8 hane 94287082 → 6 hane 287082
    assert totp.code_for_step(RFC_SECRET, 1) == "287082"


def test_match_step_accepts_current_and_drift() -> None:
    now = 59.0
    assert totp.match_step(RFC_SECRET, "287082", now=now) == 1
    assert totp.match_step(RFC_SECRET, "287082", now=now + 30) == 1  # bir adım sapma


def test_match_step_rejects_replay_and_garbage() -> None:
    assert totp.match_step(RFC_SECRET, "287082", last_used_step=1, now=59.0) is None
    assert totp.match_step(RFC_SECRET, "abcdef", now=59.0) is None
    assert totp.match_step(RFC_SECRET, "12345", now=59.0) is None
    assert totp.match_step(RFC_SECRET, "000000", now=59.0) is None


def test_match_step_ignores_spaces() -> None:
    assert totp.match_step(RFC_SECRET, "287 082", now=59.0) == 1


def test_generate_secret_is_valid_base32() -> None:
    secret = totp.generate_secret()
    assert len(secret) == 32
    assert totp.code_for_step(secret, 1).isdigit()


def test_provisioning_uri_contains_issuer_and_secret() -> None:
    uri = totp.provisioning_uri("ABC", "a@b.com", "Food App")
    assert uri.startswith("otpauth://totp/Food%20App%3Aa%40b.com?secret=ABC")
    assert "issuer=Food%20App" in uri
