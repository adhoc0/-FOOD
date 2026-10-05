"""config.monitoring.init_sentry testleri."""

import sys
import types

from config.monitoring import init_sentry


def test_does_nothing_without_dsn():
    assert init_sentry(dsn="", environment="production") is False


def test_initializes_sdk_without_pii(monkeypatch):
    calls = {}
    fake = types.ModuleType("sentry_sdk")
    fake.init = lambda **kwargs: calls.update(kwargs)
    monkeypatch.setitem(sys.modules, "sentry_sdk", fake)

    started = init_sentry(
        dsn="https://key@example.ingest.sentry.io/1",
        environment="staging",
        traces_sample_rate=0.25,
    )

    assert started is True
    assert calls["dsn"] == "https://key@example.ingest.sentry.io/1"
    assert calls["environment"] == "staging"
    assert calls["traces_sample_rate"] == 0.25
    assert calls["send_default_pii"] is False
