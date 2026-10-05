#!/bin/sh
# Bir pg_dump arşivini mevcut veritabanının ÜZERİNE geri yükler.
# Kullanım: FORCE=1 sh scripts/restore.sh /backups/db-YYYYMMDDTHHMMSSZ.dump
# Ortam: DB_HOST DB_USER DB_PASSWORD DB_NAME
set -eu

FILE="${1:?Kullanım: FORCE=1 restore.sh <dump-dosyası>}"

if [ "${FORCE:-0}" != "1" ]; then
    echo "Bu işlem '$DB_NAME' veritabanındaki verilerin üzerine yazar." >&2
    echo "Onaylamak için FORCE=1 ile yeniden çalıştırın." >&2
    exit 1
fi

export PGPASSWORD="${DB_PASSWORD:?DB_PASSWORD gerekli}"
pg_restore -h "${DB_HOST:?}" -U "${DB_USER:?}" -d "${DB_NAME:?}" \
    --clean --if-exists --no-owner --exit-on-error "$FILE"
echo "Geri yükleme tamamlandı: $FILE"
