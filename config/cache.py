"""Cache yapılandırması.

Varsayılan geliştirme cache'i process belleğindedir. Production'da Redis'e
geçiş için yalnızca backend ve location değerleri değiştirilir.
"""

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "food-cache",
    }
}
