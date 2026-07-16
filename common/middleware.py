"""Ortak güvenlik middleware'leri."""

from __future__ import annotations

from collections.abc import Callable

from django.core.cache import cache
from django.http import HttpRequest, HttpResponse


class SecurityHeadersMiddleware:
    """Tarayıcı güvenlik başlıklarını merkezi olarak ekler."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)
        response.headers.setdefault(
            "Content-Security-Policy",
            "default-src 'self'; img-src 'self' data:; style-src 'self'; "
            "script-src 'self'; font-src 'self'; connect-src 'self'; "
            "object-src 'none'; base-uri 'self'; frame-ancestors 'none'",
        )
        response.headers.setdefault(
            "Permissions-Policy",
            "camera=(), microphone=(), geolocation=()",
        )
        return response


class WriteRateLimitMiddleware:
    """Hassas POST uçlarında IP ve kullanıcı bazlı basit hız sınırı uygular."""

    LIMITS: tuple[tuple[str, int, int], ...] = (
        ("/hesap/login/", 10, 60),
        ("/hesap/register/", 5, 300),
        ("/hesap/password-reset/", 5, 300),
        ("/etkilesim/", 30, 60),
    )

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        limit = self._get_limit(request)
        if request.method == "POST" and limit is not None:
            max_requests, window_seconds = limit
            identity = self._get_identity(request)
            key = f"rate-limit:{request.path_info}:{identity}"
            count = cache.get(key, 0)
            if count >= max_requests:
                response = HttpResponse(
                    "Çok fazla istek gönderildi. Lütfen daha sonra tekrar deneyin.",
                    status=429,
                )
                response.headers["Retry-After"] = str(window_seconds)
                return response

            if not cache.add(key, 1, timeout=window_seconds):
                try:
                    cache.incr(key)
                except ValueError:
                    cache.set(key, 1, timeout=window_seconds)

        return self.get_response(request)

    def _get_limit(self, request: HttpRequest) -> tuple[int, int] | None:
        for path_prefix, max_requests, window_seconds in self.LIMITS:
            if request.path_info.startswith(path_prefix):
                return max_requests, window_seconds
        return None

    @staticmethod
    def _get_identity(request: HttpRequest) -> str:
        user = getattr(request, "user", None)
        if user is not None and user.is_authenticated:
            return f"user:{user.pk}"
        return f"ip:{request.META.get('REMOTE_ADDR', 'unknown')}"
