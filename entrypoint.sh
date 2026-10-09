#!/bin/sh
set -eu

# Uygulama komutunu çalıştırmadan önce PostgreSQL'in bağlantı kabul etmesini bekler.
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-food_db}"
DB_USER="${DB_USER:-postgres}"
MAX_RETRIES=30
RETRY_INTERVAL=2

echo "Veritabanı bağlantısı bekleniyor... ($DB_HOST:$DB_PORT)"

retries=0
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" -d "$DB_NAME" -q; do
    retries=$((retries + 1))
    if [ "$retries" -ge "$MAX_RETRIES" ]; then
        echo "HATA: Veritabanına $MAX_RETRIES deneme sonrasında bağlanılamadı!"
        exit 1
    fi

    echo "Veritabanı hazır değil, bekleniyor... ($retries/$MAX_RETRIES)"
    sleep "$RETRY_INTERVAL"
done

echo "Veritabanı bağlantısı başarılı."

if [ "$#" -eq 0 ]; then
    echo "HATA: Çalıştırılacak uygulama komutu belirtilmedi."
    exit 1
fi

exec "$@"
