#!/bin/sh

echo "Veritabanı bağlantısı bekleniyor..."

# İleride dockerize postgresql eklerseniz bekletme mekanizması kurulabilir.
# Şimdilik direkt geçiyoruz.

echo "Statik dosyalar toplanıyor..."
python manage.py collectstatic --noinput

echo "Veritabanı migration işlemleri uygulanıyor..."
python manage.py migrate

echo "Gunicorn başlatılıyor..."
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3
