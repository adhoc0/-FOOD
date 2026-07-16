"""Güvenlik middleware'leri için birim testleri."""

from django.core.cache import cache
from django.http import HttpResponse
from django.test import RequestFactory

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
