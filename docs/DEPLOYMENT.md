# DEPLOYMENT

## Amaç

Bu doküman projenin geliştirme, test ve production ortamlarında nasıl dağıtılacağını tanımlar.

Amaç;

- Güvenli
- Tekrarlanabilir
- Otomatikleştirilebilir
- Ölçeklenebilir
- Bakımı kolay

bir deployment süreci oluşturmaktır.

---

# Ortamlar

## Development

Yerel geliştirme ortamıdır.

Özellikleri

- DEBUG=True
- Docker kullanılabilir
- PostgreSQL
- Local Media
- Local Static

---

## Testing

Test ortamıdır.

Özellikleri

- DEBUG=False
- Ayrı veritabanı
- Test verileri
- Test logları

---

## Staging

Production'ın birebir kopyasıdır.

Yeni özellikler önce burada test edilir.

Gerçek kullanıcı kullanılmaz.

---

## Production

Canlı ortamdır.

DEBUG kesinlikle kapalıdır.

---

# Kullanılan Teknolojiler

Backend

- Python
- Django

Veritabanı

- PostgreSQL

Web Server

- Nginx

Application Server

- Gunicorn

Container

- Docker
- Docker Compose

SSL

- Let's Encrypt

---

# Deployment Mimarisi

Client

↓

Nginx

↓

Gunicorn

↓

Django

↓

PostgreSQL

---

# Docker

Her servis ayrı container içerisinde çalışacaktır.

Örnek

- web
- nginx
- postgres
- redis (gelecekte)
- celery (gelecekte)

---

# Environment Değişkenleri

Tüm gizli bilgiler

.env

dosyasında tutulacaktır.

Örneğin

```
SECRET_KEY

DEBUG

DATABASE_URL

ALLOWED_HOSTS

EMAIL_HOST

EMAIL_PORT

EMAIL_USER

EMAIL_PASSWORD
```

Hiçbiri Git içerisine gönderilmez.

---

# Production Ayarları

DEBUG=False

ALLOWED_HOSTS tanımlı olmalıdır.

SECRET_KEY güvenli olmalıdır.

HTTPS zorunludur.

CSRF güvenli olmalıdır.

SESSION_COOKIE_SECURE=True

CSRF_COOKIE_SECURE=True

SECURE_SSL_REDIRECT=True

---

# Static Dosyalar

collectstatic kullanılacaktır.

Static dosyalar Nginx üzerinden servis edilir.

Django static dosya sunmaz.

---

# Media Dosyaları

Media dosyaları

MEDIA_ROOT

üzerinde tutulacaktır.

Gelecekte

Amazon S3

veya

Cloudflare R2

kullanılabilir.

---

# Gunicorn

Gunicorn uygulama sunucusudur.

Örnek

```
gunicorn core.wsgi:application
```

Worker sayısı

Sunucu donanımına göre belirlenir.

---

# Nginx

Nginx

Reverse Proxy olarak çalışacaktır.

Görevleri

- HTTPS
- Static
- Media
- Gzip
- Reverse Proxy
- Cache Header

---

# HTTPS

HTTPS zorunludur.

TLS 1.2+

kullanılacaktır.

HTTP otomatik HTTPS'e yönlendirilir.

---

# Güvenlik

Production'da

DEBUG=False

zorunludur.

Admin paneli korunmalıdır.

Rate Limiting uygulanmalıdır.

Güvenlik Header'ları aktif olmalıdır.

---

# Loglama

Error Log

Access Log

Application Log

ayrı tutulacaktır.

Log dosyaları düzenli döndürülmelidir.

(Log Rotation)

---

# Monitoring

İleride

- Prometheus
- Grafana
- Sentry

eklenebilir.

---

# Cache

Gelecekte

Redis

kullanılacaktır.

Cache;

- Sık kullanılan sorgular
- Sayfa parçaları
- Session
- Arama sonuçları

için kullanılacaktır.

---

# Celery

Gelecekte

Celery

kullanılacaktır.

Arka plan görevleri

- E-posta gönderimi
- Görsel optimizasyonu
- Sitemap oluşturma
- Cache temizleme

---

# Backup

Veritabanı

Günlük otomatik yedek.

Media

Haftalık yedek.

Yedekler farklı sunucuda saklanmalıdır.

Geri yükleme test edilmelidir.

---

# Migration

Deployment sırasında

```
python manage.py migrate
```

çalıştırılır.

Migration dosyaları manuel değiştirilmez.

---

# Collectstatic

Deployment sırasında

```
python manage.py collectstatic --noinput
```

çalıştırılır.

---

# Deployment Sırası

1. Kod sunucuya gönderilir.

2. Docker image oluşturulur.

3. Container başlatılır.

4. Migration çalıştırılır.

5. Collectstatic çalıştırılır.

6. Gunicorn yeniden başlatılır.

7. Nginx yeniden yüklenir.

8. Sistem sağlık kontrolü yapılır.

---

# Health Check

Deployment sonrası kontrol edilir.

- Sunucu çalışıyor mu?
- Veritabanı bağlantısı var mı?
- Static dosyalar geliyor mu?
- Media dosyaları çalışıyor mu?
- Admin paneli açılıyor mu?
- HTTPS aktif mi?

---

# Rollback

Deployment başarısız olursa

Önceki Docker image

ile sistem geri alınır.

Veritabanı geri yükleme gerekiyorsa backup kullanılır.

---

# Performans

Gzip açık olmalıdır.

HTTP/2 kullanılmalıdır.

Static cache aktif olmalıdır.

Image compression uygulanmalıdır.

Lazy Loading kullanılmalıdır.

---

# SEO

robots.txt

sitemap.xml

Canonical URL

OpenGraph

Production ortamında aktif olmalıdır.

---

# CI/CD (Gelecekte)

GitHub Actions kullanılacaktır.

Pipeline

1. Lint

2. Format Kontrolü

3. Testler

4. Build

5. Docker Image

6. Deploy

---

# Yasaklar

Production'da DEBUG=True kullanmak.

SECRET_KEY'i Git'e eklemek.

.env dosyasını paylaşmak.

Static dosyaları Django üzerinden sunmak.

HTTPS kullanmamak.

Migration dosyalarını manuel düzenlemek.

Sunucuda manuel kod değiştirmek.

Production veritabanında doğrudan değişiklik yapmak.

Backup almadan deployment yapmak.

Test edilmemiş kodu production'a göndermek.

Deployment sırasında logları kontrol etmemek.

Health check yapmadan deployment'ı tamamlanmış kabul etmek.