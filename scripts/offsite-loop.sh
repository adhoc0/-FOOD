#!/bin/sh
# Yerel yedekleri uzak depolamaya (S3/B2/SFTP vb., rclone) kopyalar.
# Her gün OFFSITE_HOUR_UTC (varsayılan 04:00 UTC) çalışır; backup-loop 03:00'te yedek aldıktan sonra.
# Ortam: OFFSITE_REMOTE (örn. "offsite:bucket/food"), rclone yapılandırması RCLONE_CONFIG_* ile.
set -u

HOUR="${OFFSITE_HOUR_UTC:-4}"
REMOTE="${OFFSITE_REMOTE:?OFFSITE_REMOTE gerekli}"
RETENTION_DAYS="${OFFSITE_RETENTION_DAYS:-30}"

while :; do
    NOW="$(date -u +%s)"
    NEXT=$(( NOW / 86400 * 86400 + HOUR * 3600 ))
    [ "$NEXT" -le "$NOW" ] && NEXT=$(( NEXT + 86400 ))
    echo "Sonraki dış kopya: $(date -u -d "@$NEXT" +%Y-%m-%dT%H:%M:%SZ)"
    sleep $(( NEXT - NOW ))
    # copy: yerelde silinen eski dosyalar uzakta kalır; uzak tarafı yaşa göre ayrıca temizleriz.
    if rclone copy /backups "$REMOTE" --include 'db-*.dump' --include 'media-*.tar.gz'; then
        rclone delete "$REMOTE" --min-age "${RETENTION_DAYS}d" || echo "UYARI: uzak temizlik başarısız" >&2
        echo "Dış kopya tamamlandı."
    else
        echo "UYARI: dış kopya başarısız oldu" >&2
    fi
done
