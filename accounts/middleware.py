from __future__ import annotations

from collections.abc import Callable
from typing import cast
from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from accounts.models import CustomUser
from accounts.services import mfa_service


class StaffMFAMiddleware:
    """Yönetim paneline yalnızca 2FA doğrulaması yapmış personeli alır."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        if (
            request.path.startswith(f"/{settings.ADMIN_URL}")
            and mfa_service.requires_mfa(request.user)
            and not mfa_service.is_verified(request)
        ):
            user = cast(CustomUser, request.user)
            name = (
                "accounts:mfa_verify"
                if mfa_service.has_confirmed_device(user)
                else "accounts:mfa_setup"
            )
            query = urlencode({"next": request.get_full_path()})
            return redirect(f"{reverse(name)}?{query}")

        return self.get_response(request)
