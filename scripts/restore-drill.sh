#!/bin/sh
# Geri yükleme tatbikatı: en son DB yedeğini GEÇİCİ bir veritabanına yükler, tablo sayısını ve
# recipes_recipe satır sayısını raporlar, sonra geçici veritabanını siler. Üretim verisine dokunmaz.
# Ortam: DB_HOST DB_USER DB_PASSWORD [BACKUP_DIR]
set -eu

BACKUP_DIR="${BACKUP_DIR:-/backups}"
export PGPASSWORD="${DB_PASSWORD:?DB_PASSWORD gerekli}"
DUMP="$(ls -1t "$BACKUP_DIR"/db-*.dump 2>/dev/null | head -n 1)"
[ -n "$DUMP" ] || { echo "HATA: yedek bulunamadı" >&2; exit 1; }

TMPDB="restore_drill_$(date -u +%s)"
PSQL="psql -h ${DB_HOST:?} -U ${DB_USER:?} -d postgres -v ON_ERROR_STOP=1 -tA"
trap '$PSQL -c "DROP DATABASE IF EXISTS $TMPDB" >/dev/null 2>&1 || true' EXIT

echo "Yedek: $DUMP -> $TMPDB"
$PSQL -c "CREATE DATABASE $TMPDB"
pg_restore -h "$DB_HOST" -U "$DB_USER" -d "$TMPDB" --no-owner --exit-on-error "$DUMP"

TABLES="$(psql -h "$DB_HOST" -U "$DB_USER" -d "$TMPDB" -tAc "SELECT count(*) FROM information_schema.tables WHERE table_schema='public'")"
RECIPES="$(psql -h "$DB_HOST" -U "$DB_USER" -d "$TMPDB" -tAc "SELECT count(*) FROM recipes_recipe" 2>/dev/null || echo "?")"
echo "Tablo sayısı: $TABLES, tarif sayısı: $RECIPES"
[ "$TABLES" -gt 0 ] || { echo "HATA: geri yüklenen veritabanı boş" >&2; exit 1; }
echo "Tatbikat başarılı."
