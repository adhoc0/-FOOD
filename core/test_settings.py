"""Test ortamı için güvenli ve tekrarlanabilir Django ayarları."""

from core import settings as base_settings

# Ana ayar modülündeki tüm Django ayarlarını açıkça kopyalıyoruz. Böylece test
# ortamı production ayarlarından kopuk bir ikinci yapılandırma ağacına dönüşmez.
for _setting_name in dir(base_settings):
    if _setting_name.isupper():
        globals()[_setting_name] = getattr(base_settings, _setting_name)


DEBUG = False
SECRET_KEY = "test-only-secret-key-with-more-than-fifty-characters-123456"
ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
