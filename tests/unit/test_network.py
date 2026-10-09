"""İstemci IP çözümlemesi için birim testleri."""

from django.test import RequestFactory

from common.network import UNKNOWN_CLIENT_IP, get_client_ip


def test_uses_remote_address_when_no_proxy_is_trusted() -> None:
    request = RequestFactory().get(
        "/",
        REMOTE_ADDR="10.0.0.5",
        HTTP_X_FORWARDED_FOR="203.0.113.9",
    )

    assert get_client_ip(request, trusted_proxy_count=0) == "10.0.0.5"


def test_reads_last_forwarded_address_for_single_trusted_proxy() -> None:
    request = RequestFactory().get(
        "/",
        REMOTE_ADDR="172.18.0.3",
        HTTP_X_FORWARDED_FOR="198.51.100.7, 203.0.113.9",
    )

    assert get_client_ip(request, trusted_proxy_count=1) == "203.0.113.9"


def test_ignores_client_supplied_leading_addresses() -> None:
    request = RequestFactory().get(
        "/",
        REMOTE_ADDR="172.18.0.3",
        HTTP_X_FORWARDED_FOR="1.2.3.4, 203.0.113.9",
    )

    assert get_client_ip(request, trusted_proxy_count=1) != "1.2.3.4"


def test_falls_back_to_remote_address_when_header_is_shorter_than_proxy_count() -> None:
    request = RequestFactory().get(
        "/",
        REMOTE_ADDR="172.18.0.3",
        HTTP_X_FORWARDED_FOR="203.0.113.9",
    )

    assert get_client_ip(request, trusted_proxy_count=2) == "172.18.0.3"


def test_returns_unknown_when_remote_address_is_missing() -> None:
    request = RequestFactory().get("/")
    request.META.pop("REMOTE_ADDR", None)

    assert get_client_ip(request, trusted_proxy_count=0) == UNKNOWN_CLIENT_IP
