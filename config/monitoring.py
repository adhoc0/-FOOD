"""Hata izleme (Sentry) başlatıcısı.

`SENTRY_DSN` tanımlı değilse hiçbir şey yapmaz; `sentry-sdk` yalnızca
production bağımlılığıdır ve bu yüzden import ihtiyaç anında yapılır.
"""

from __future__ import annotations


def init_sentry(
    *,
    dsn: str,
    environment: str,
    traces_sample_rate: float = 0.0,
) -> bool:
    """Sentry'yi başlatır. Başlatıldıysa True döner."""

    if not dsn:
        return False

    import sentry_sdk

    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        traces_sample_rate=traces_sample_rate,
        # Kullanıcı IP/e-posta gibi kişisel veriler Sentry'ye gönderilmez.
        send_default_pii=False,
    )
    return True
