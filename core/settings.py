"""
Django settings — Türkiye Yöresel Yemekleri

Django 6.0.6

Hassas veriler .env dosyasından okunur.
.env.example dosyasını referans olarak kullanın.

Mimari Notlar:
─────────────────────────────────────────────
- INSTALLED_APPS üç gruba ayrıldı: Django, Third Party, Local
  → Hangi dependency'nin nereden geldiği ilk bakışta anlaşılır
- Güvenlik ayarları DEBUG=False olduğunda otomatik devreye girer
  → Production'a geçerken unutma riski sıfır
- i18n altyapısı hazır (LANGUAGES, LOCALE_PATHS, LocaleMiddleware)
  → İleride çoklu dil eklemek tek komutla mümkün
"""

from pathlib import Path
# pyrefly: ignore [missing-import]
from decouple import config, Csv


# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent


# ─────────────────────────────────────────────
# Security
# ─────────────────────────────────────────────
SECRET_KEY = config('SECRET_KEY', default='django-insecure-m+z#1$f=y-4&3f6+l#q+n&n9v&n9v&n9v&n9v&n9v&n9v&n9v')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())


# ─────────────────────────────────────────────
# Application definition
# ─────────────────────────────────────────────
# Neden üçe ayırdık?
# Django apps: Framework ile gelen, her projede olan uygulamalar
# Third party: pip ile yüklenen dış kütüphaneler
# Local apps: Bizim yazdığımız uygulamalar
# → Bir bakışta "bu dependency nereden geliyor?" sorusuna cevap verir

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',      # SEO: XML sitemap
    'django.contrib.humanize',      # Template: "5 dakika önce" gibi formatlar
]

THIRD_PARTY_APPS = [
    # İleride buraya DRF, django-axes vb. eklenecek
]

LOCAL_APPS = [
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'provinces.apps.ProvincesConfig',
    'recipes.apps.RecipesConfig',
    'interactions.apps.InteractionsConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# ─────────────────────────────────────────────
# Custom User Model
# ─────────────────────────────────────────────
# KRITIK: Bu ayar ilk migration'dan ÖNCE yapılmalıdır.
# Sonradan değiştirmek tüm migration geçmişini bozar.

AUTH_USER_MODEL = 'accounts.CustomUser'


# ─────────────────────────────────────────────
# Middleware
# ─────────────────────────────────────────────
# Sıralama önemli! Django middleware'leri yukarıdan aşağıya
# request'te, aşağıdan yukarıya response'ta çalışır.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # HTTPS yönlendirme, HSTS
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session yönetimi
    'django.middleware.locale.LocaleMiddleware',             # i18n: Dil algılama
    'django.middleware.common.CommonMiddleware',             # URL normalizasyonu
    'django.middleware.csrf.CsrfViewMiddleware',             # CSRF koruması
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # request.user
    'django.contrib.messages.middleware.MessageMiddleware',   # Flash mesajlar
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking koruması
]


# ─────────────────────────────────────────────
# URL Configuration
# ─────────────────────────────────────────────
ROOT_URLCONF = 'core.urls'


# ─────────────────────────────────────────────
# Templates
# ─────────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Proje genelindeki template'ler burada aranır
        'DIRS': [BASE_DIR / 'templates'],
        # Her app'in kendi templates/ klasörü de taranır
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',     # debug değişkeni
                'django.template.context_processors.request',   # request objesi
                'django.contrib.auth.context_processors.auth',  # user, perms
                'django.contrib.messages.context_processors.messages',  # mesajlar
                'django.template.context_processors.i18n',      # i18n desteği
            ],
        },
    },
]


# ─────────────────────────────────────────────
# WSGI / ASGI
# ─────────────────────────────────────────────
WSGI_APPLICATION = 'core.wsgi.application'


# ─────────────────────────────────────────────
# Database
# ─────────────────────────────────────────────
# PostgreSQL baştan kullanıyoruz (kullanıcı tercihi).
# psycopg3 (psycopg paketi) kullanılıyor — Django 4.2+ destekler.
#
# Neden SQLite değil?
# - Full-text search, JSON alanları, concurrent write desteği
# - Production ile aynı engine = "bende çalışıyordu" sorunu yok
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='food_db'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'connect_timeout': 5,
        }
    }
}


# ─────────────────────────────────────────────
# Password Validation
# ─────────────────────────────────────────────
# Django'nun built-in şifre doğrulayıcıları.
# Minimum uzunluk, yaygın şifre kontrolü, kullanıcı adı benzerliği,
# sadece rakam kontrolü.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# ─────────────────────────────────────────────
# Internationalization (i18n)
# ─────────────────────────────────────────────
# Şimdilik Türkçe, ileride İngilizce de eklenecek.
# LocaleMiddleware + LANGUAGES + LOCALE_PATHS ile
# çoklu dil altyapısı hazır.
LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

LANGUAGES = [
    ('tr', 'Türkçe'),
    ('en', 'English'),
]


# ─────────────────────────────────────────────
# Static Files (CSS, JavaScript, Images)
# ─────────────────────────────────────────────
# STATIC_URL: Tarayıcıdan erişim URL'i
# STATICFILES_DIRS: Geliştirme sırasında ek static klasörler
# STATIC_ROOT: collectstatic komutuyla dosyaların toplandığı yer (production)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ─────────────────────────────────────────────
# Media Files (User/Admin Uploads)
# ─────────────────────────────────────────────
# Tarif resimleri, profil fotoğrafları vb. buraya yüklenir.
# Production'da Nginx tarafından servis edilecek.
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ─────────────────────────────────────────────
# Default Primary Key
# ─────────────────────────────────────────────
# BigAutoField: 64-bit integer. Binlerce tarif ve kullanıcı
# için yeterli (9.2 quintillion'a kadar). AutoField (32-bit)
# büyük ölçekte sorun çıkarabilir.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ─────────────────────────────────────────────
# Authentication URLs
# ─────────────────────────────────────────────
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'pages:home'
LOGOUT_REDIRECT_URL = 'pages:home'


# ─────────────────────────────────────────────
# Security Settings (Production Only)
# ─────────────────────────────────────────────
# Bu ayarlar sadece DEBUG=False olduğunda aktif olur.
# Development'ta HTTPS olmadığı için aktif olursa
# tarayıcı siteye erişemez.
if not DEBUG:
    # ── HTTPS Zorlama ──
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # ── HSTS (HTTP Strict Transport Security) ──
    # Tarayıcıya "bu siteye sadece HTTPS ile bağlan" der.
    # 1 yıl = 31536000 saniye
    SECURE_HSTS_SECONDS = 31_536_000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # ── Cookie Güvenliği ──
    SESSION_COOKIE_SECURE = True    # Session cookie sadece HTTPS
    CSRF_COOKIE_SECURE = True       # CSRF cookie sadece HTTPS
    SESSION_COOKIE_HTTPONLY = True   # JavaScript session cookie'ye erişemez

    # ── İçerik Güvenliği ──
    # Django 4.0+ varsayılanları zaten güvenli, ama
    # açık tutmak iyi bir pratik.
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

# ─────────────────────────────────────────────
# CSRF Trusted Origins
# ─────────────────────────────────────────────
# Django 4.0+ HTTPS üzerinde CSRF doğrulaması için gereklidir.
# Production'da gerçek domain eklenmeli.
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://localhost,http://127.0.0.1',
    cast=Csv(),
)


# ─────────────────────────────────────────────
# Email Settings (Development)
# ─────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ─────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────
# Konsol + dosya çıktısı. Production'da Sentry veya benzeri
# bir hata izleme servisi eklenebilir.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': config('DJANGO_LOG_LEVEL', default='INFO'),
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}


# ─────────────────────────────────────────────
# Cache
# ─────────────────────────────────────────────
# Şimdilik local-memory cache. Production'da Redis önerilir:
# pip install django-redis → 'django_redis.cache.RedisCache'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'food-cache',
    }
}
