#!/bin/sh
# PostgreSQL (pg_dump, custom format) ve medya yedeği alır, eskileri siler.
# Ortam: DB_HOST DB_USER DB_PASSWORD DB_NAME [BACKUP_DIR] [MEDIA_DIR] [RETENTION_DAYS]
set -eu

BACKUP_DIR="${BACKUP_DIR:-/backups}"
MEDIA_DIR="${MEDIA_DIR:-/media}"
RETENTION_DAYS="${RETENTION_DAYS:-14}"
TS="$(date -u +%Y%m%dT%H%M%SZ)"

export PGPASSWORD="${DB_PASSWORD:?DB_PASSWORD gerekli}"
mkdir -p "$BACKUP_DIR"

DUMP="$BACKUP_DIR/db-$TS.dump"
echo "[$TS] Veritabanı yedeği alınıyor: $DUMP"
pg_dump -h "${DB_HOST:?}" -U "${DB_USER:?}" -d "${DB_NAME:?}" -Fc -f "$DUMP.tmp"

# Arşivin okunabilir olduğunu doğrula; bozuksa yedeği kabul etme.
if ! pg_restore -l "$DUMP.tmp" > /dev/null; then
    echo "HATA: yedek arşivi doğrulanamadı, siliniyor." >&2
    rm -f "$DUMP.tmp"
    exit 1
fi
mv "$DUMP.tmp" "$DUMP"

if [ -d "$MEDIA_DIR" ] && [ -n "$(ls -A "$MEDIA_DIR" 2>/dev/null)" ]; then
    MEDIA="$BACKUP_DIR/media-$TS.tar.gz"
    echo "[$TS] Medya yedeği alınıyor: $MEDIA"
    tar -czf "$MEDIA.tmp" -C "$MEDIA_DIR" .
    mv "$MEDIA.tmp" "$MEDIA"
fi

echo "[$TS] $RETENTION_DAYS günden eski yedekler siliniyor"
find "$BACKUP_DIR" -type f \( -name 'db-*.dump' -o -name 'media-*.tar.gz' \) \
    -mtime +"$RETENTION_DAYS" -delete

echo "[$TS] Yedekleme tamamlandı."
