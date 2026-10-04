"""Ağ katmanı yardımcıları."""

from __future__ import annotations

from django.http import HttpRequest

UNKNOWN_CLIENT_IP = "unknown"


def get_client_ip(request: HttpRequest, *, trusted_proxy_count: int) -> str:
    """İstemci IP adresini güvenilen proxy sayısına göre çözer.

    Güvenilen her proxy X-Forwarded-For sonuna bağlandığı istemci adresini ekler.
    Bu yüzden adres, soldan değil sağdan sayılır; soldaki kayıtlar istemci
    tarafından taklit edilebilir.
    """
    remote_address = str(request.META.get("REMOTE_ADDR", UNKNOWN_CLIENT_IP))
    if trusted_proxy_count <= 0:
        return remote_address

    forwarded_addresses = [
        address.strip()
        for address in request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")
        if address.strip()
    ]
    if len(forwarded_addresses) < trusted_proxy_count:
        return remote_address

    return str(forwarded_addresses[-trusted_proxy_count])
