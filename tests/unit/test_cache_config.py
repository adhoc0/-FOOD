"""config.cache: REDIS_URL'e göre backend seçimi."""

import importlib

import config.cache as cache_config


def _reload(monkeypatch, url):
    if url is None:
        monkeypatch.delenv("REDIS_URL", raising=False)
    else:
        monkeypatch.setenv("REDIS_URL", url)
    return importlib.reload(cache_config)


def test_uses_locmem_without_redis_url(monkeypatch):
    module = _reload(monkeypatch, None)

    assert module.CACHES["default"]["BACKEND"].endswith("LocMemCache")
    monkeypatch.undo()
    importlib.reload(cache_config)


def test_uses_redis_when_url_is_set(monkeypatch):
    module = _reload(monkeypatch, "redis://redis:6379/1")

    default = module.CACHES["default"]
    assert default["BACKEND"] == "django.core.cache.backends.redis.RedisCache"
    assert default["LOCATION"] == "redis://redis:6379/1"
    monkeypatch.undo()
    importlib.reload(cache_config)
