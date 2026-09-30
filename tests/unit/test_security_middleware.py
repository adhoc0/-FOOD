"""Güvenlik middleware'leri için birim testleri."""

from django.core.cache import cache
from django.http import HttpResponse
from django.test import RequestFactory, override_settings

from common.middleware import SecurityHeadersMiddleware, WriteRateLimitMiddleware


def test_security_headers_are_added() -> None:
    request = RequestFactory().get("/")
    middleware = SecurityHeadersMiddleware(lambda _request: HttpResponse())

    response = middleware(request)

    assert response["Content-Security-Policy"].startswith("default-src 'self'")
    assert response["Permissions-Policy"] == (
        "camera=(), microphone=(), geolocation=()"
    )


def test_write_rate_limit_returns_429_after_limit() -> None:
    cache.clear()
    request_factory = RequestFactory()
    middleware = WriteRateLimitMiddleware(lambda _request: HttpResponse())

    for _ in range(10):
        response = middleware(request_factory.post("/hesap/login/"))
        assert response.status_code == 200

    limited_response = middleware(request_factory.post("/hesap/login/"))

    assert limited_response.status_code == 429
    assert limited_response["Retry-After"] == "60"
    cache.clear()


@override_settings(NUM_PROXIES=1)
def test_rate_limit_separates_clients_behind_trusted_proxy() -> None:
    cache.clear()
    request_factory = RequestFactory()
    middleware = WriteRateLimitMiddleware(lambda _request: HttpResponse())

    for _ in range(10):
        middleware(
            request_factory.post(
                "/hesap/login/",
                REMOTE_ADDR="172.18.0.3",
                HTTP_X_FORWARDED_FOR="203.0.113.9",
            )
        )

    blocked = middleware(
        request_factory.post(
            "/hesap/login/",
            REMOTE_ADDR="172.18.0.3",
            HTTP_X_FORWARDED_FOR="203.0.113.9",
        )
    )
    other_client = middleware(
        request_factory.post(
            "/hesap/login/",
            REMOTE_ADDR="172.18.0.3",
            HTTP_X_FORWARDED_FOR="198.51.100.20",
        )
    )

    assert blocked.status_code == 429
    assert other_client.status_code == 200
    cache.clear()


@override_settings(NUM_PROXIES=1)
def test_rate_limit_cannot_be_bypassed_with_spoofed_header() -> None:
    cache.clear()
    request_factory = RequestFactory()
    middleware = WriteRateLimitMiddleware(lambda _request: HttpResponse())

    for attempt in range(10):
        middleware(
            request_factory.post(
                "/hesap/login/",
                REMOTE_ADDR="172.18.0.3",
                HTTP_X_FORWARDED_FOR=f"10.9.9.{attempt}, 203.0.113.9",
            )
        )

    spoofed = middleware(
        request_factory.post(
            "/hesap/login/",
            REMOTE_ADDR="172.18.0.3",
            HTTP_X_FORWARDED_FOR="10.9.9.99, 203.0.113.9",
        )
    )

    assert spoofed.status_code == 429
    cache.clear()
