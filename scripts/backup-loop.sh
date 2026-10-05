#!/bin/sh
# Her gün 03:00 UTC'de backup.sh çalıştırır. Başarısız çalıştırma döngüyü durdurmaz.
set -u

HOUR="${BACKUP_HOUR_UTC:-3}"

while :; do
    NOW="$(date -u +%s)"
    TODAY_START=$(( NOW / 86400 * 86400 ))
    NEXT=$(( TODAY_START + HOUR * 3600 ))
    if [ "$NEXT" -le "$NOW" ]; then
        NEXT=$(( NEXT + 86400 ))
    fi
    echo "Sonraki yedek: $(date -u -d "@$NEXT" +%Y-%m-%dT%H:%M:%SZ)"
    sleep $(( NEXT - NOW ))
    sh /scripts/backup.sh || echo "UYARI: yedekleme başarısız oldu" >&2
done
