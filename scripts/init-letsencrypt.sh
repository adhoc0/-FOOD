#!/bin/sh
# İlk kurulumda Let's Encrypt sertifikasını alır.
# Nginx 443 bloğu sertifika dosyası olmadan başlamaz; bu yüzden önce geçici
# (self-signed) sertifika yazılır, Nginx başlatılır, gerçek sertifika webroot
# ile alınır ve Nginx yeniden yüklenir.
#
# Kullanım: sh scripts/init-letsencrypt.sh   (.env.prod gerekli)
set -eu

COMPOSE="docker compose -f docker-compose.prod.yml --env-file .env.prod"

set -a
. ./.env.prod
set +a

: "${DOMAIN:?DOMAIN .env.prod içinde tanımlanmalıdır}"
: "${LETSENCRYPT_EMAIL:?LETSENCRYPT_EMAIL .env.prod içinde tanımlanmalıdır}"

CERT_DIR="/etc/letsencrypt/live/${DOMAIN}"

echo "==> Geçici sertifika oluşturuluyor"
$COMPOSE run --rm --entrypoint /bin/sh certbot -c "
  mkdir -p ${CERT_DIR} &&
  apk add --no-cache openssl >/dev/null 2>&1 || true
  openssl req -x509 -nodes -newkey rsa:2048 -days 1 \
    -keyout ${CERT_DIR}/privkey.pem -out ${CERT_DIR}/fullchain.pem \
    -subj '/CN=${DOMAIN}'"

echo "==> Servisler başlatılıyor"
$COMPOSE up -d nginx

echo "==> Geçici sertifika siliniyor"
$COMPOSE run --rm --entrypoint /bin/sh certbot -c "
  rm -rf /etc/letsencrypt/live/${DOMAIN} \
         /etc/letsencrypt/archive/${DOMAIN} \
         /etc/letsencrypt/renewal/${DOMAIN}.conf"

echo "==> Gerçek sertifika isteniyor"
$COMPOSE run --rm --entrypoint certbot certbot certonly --webroot \
  -w /var/www/certbot -d "${DOMAIN}" \
  --email "${LETSENCRYPT_EMAIL}" --agree-tos --no-eff-email

echo "==> Nginx yeniden yükleniyor"
$COMPOSE exec nginx nginx -s reload

$COMPOSE up -d
echo "Tamamlandı: https://${DOMAIN}"
