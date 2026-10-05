#!/bin/sh
# Sunucuda registry'den imaj çekip güncelleme yapar.
# Kullanım: scripts/deploy.sh [etiket]      (varsayılan: latest)
#           scripts/deploy.sh --rollback    (önceki etiketle geri dön)
# Ön koşul: .env.prod mevcut; özel paket ise `docker login ghcr.io` yapılmış.
set -eu

COMPOSE="docker compose -f docker-compose.prod.yml --env-file .env.prod"
STATE=".deploy-state"
IMAGE_BASE="${FOOD_IMAGE_BASE:-ghcr.io/adhoc0/food-web}"

current_tag() { [ -f "$STATE" ] && cat "$STATE" || echo ""; }

if [ "${1:-}" = "--rollback" ]; then
    TAG="$(cat "$STATE.prev" 2>/dev/null || true)"
    [ -n "$TAG" ] || { echo "HATA: önceki etiket kayıtlı değil" >&2; exit 1; }
else
    TAG="${1:-latest}"
fi

PREV="$(current_tag)"
export FOOD_IMAGE="$IMAGE_BASE:$TAG"
echo "Dağıtım: $FOOD_IMAGE"

$COMPOSE pull web initialize
$COMPOSE up -d --remove-orphans

echo "Sağlık kontrolü bekleniyor..."
for _ in $(seq 1 30); do
    STATUS="$($COMPOSE ps --format '{{.Health}}' web 2>/dev/null | head -n 1)"
    if [ "$STATUS" = "healthy" ]; then
        [ -n "$PREV" ] && [ "$PREV" != "$TAG" ] && echo "$PREV" > "$STATE.prev"
        echo "$TAG" > "$STATE"
        echo "Dağıtım başarılı: $TAG"
        exit 0
    fi
    sleep 5
done

echo "HATA: web sağlıklı olmadı. Geri almak için: scripts/deploy.sh --rollback" >&2
exit 1
