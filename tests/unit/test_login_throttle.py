"""accounts.services.login_throttle testleri."""

import pytest
from django.core.cache import cache

from accounts.services import login_throttle


@pytest.fixture(autouse=True)
def _clear_cache():
    cache.clear()
    yield
    cache.clear()


def test_locks_after_max_failures():
    for _ in range(login_throttle.MAX_FAILED_ATTEMPTS - 1):
        login_throttle.register_failure("ayse")
        assert not login_throttle.is_locked("ayse")

    login_throttle.register_failure("ayse")

    assert login_throttle.is_locked("ayse")


def test_username_is_normalized():
    for _ in range(login_throttle.MAX_FAILED_ATTEMPTS):
        login_throttle.register_failure("  Ayse ")

    assert login_throttle.is_locked("ayse")


def test_other_users_are_unaffected():
    for _ in range(login_throttle.MAX_FAILED_ATTEMPTS):
        login_throttle.register_failure("ayse")

    assert not login_throttle.is_locked("mehmet")


def test_reset_clears_counter():
    for _ in range(login_throttle.MAX_FAILED_ATTEMPTS):
        login_throttle.register_failure("ayse")

    login_throttle.reset("ayse")

    assert not login_throttle.is_locked("ayse")


def test_register_failure_returns_running_count():
    assert login_throttle.register_failure("ayse") == 1
    assert login_throttle.register_failure("ayse") == 2
