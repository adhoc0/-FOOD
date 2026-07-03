#!/bin/sh
set -e

# ─────────────────────────────────────────────
# Veritabanı bağlantısı bekle (DB_HOST ve DB_PORT kullanır)
# ─────────────────────────────────────────────
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
MAX_RETRIES=30
RETRY_INTERVAL=2

echo "Veritabanı bağlantısı bekleniyor... ($DB_HOST:$DB_PORT)"

retries=0
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -q 2>/dev/null; do
    retries=$((retries + 1))
    if [ "$retries" -ge "$MAX_RETRIES" ]; then
        echo "HATA: Veritabanına $MAX_RETRIES deneme sonrası bağlanılamadı!"
        exit 1
    fi
    echo "Veritabanı hazır değil, bekleniyor... ($retries/$MAX_RETRIES)"
    sleep "$RETRY_INTERVAL"
done

echo "Veritabanı bağlantısı başarılı!"

# ─────────────────────────────────────────────
# Django işlemleri
# ─────────────────────────────────────────────
echo "Statik dosyalar toplanıyor..."
python manage.py collectstatic --noinput

echo "Veritabanı migration işlemleri uygulanıyor..."
python manage.py migrate --noinput

echo "Gunicorn başlatılıyor..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
