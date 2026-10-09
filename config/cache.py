"""Cache yapılandırması.

`REDIS_URL` tanımlıysa Django'nun yerleşik Redis backend'i kullanılır; böylece
rate limiting gibi cache'e dayanan özellikler tüm Gunicorn worker'ları arasında
paylaşılır. Tanımlı değilse (geliştirme/test) process belleği kullanılır.
"""

from decouple import config

_REDIS_URL = config("REDIS_URL", default="")

if _REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": _REDIS_URL,
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "food-cache",
        }
    }
