---
name: deployment
description: Django projesi için deployment kuralları ve production standartları.
---

# Deployment

## Genel Kurallar

- Deployment işlemleri tekrarlanabilir olmalıdır.
- Production ortamında manuel değişiklik yapılmamalıdır.
- Tüm değişiklikler Git üzerinden yönetilmelidir.
- Deployment öncesinde testler başarılı olmalıdır.

---

## Ortamlar

- local
- development
- staging
- production

Her ortam birbirinden bağımsızdır.

---

## Environment Variables

Hiçbir gizli bilgi kod içerisinde tutulmaz.

Örneğin;

- SECRET_KEY
- DB_PASSWORD
- API_KEY
- SMTP_PASSWORD
- AWS_SECRET_KEY

yalnızca .env dosyasında bulunmalıdır.

---

## Django

Production ortamında aşağıdaki ayarlar zorunludur.

DEBUG=False

ALLOWED_HOSTS tanımlı olmalıdır.

SECRET_KEY environment variable üzerinden okunmalıdır.

CSRF güvenliği aktif olmalıdır.

SESSION güvenliği aktif olmalıdır.

---

## Static Files

Deployment öncesinde

python manage.py collectstatic

çalıştırılmalıdır.

---

## Migration

Deployment öncesinde

python manage.py makemigrations

çalıştırılmaz.

Sadece

python manage.py migrate

çalıştırılır.

Production ortamında yeni migration oluşturulmaz.

---

## PostgreSQL

- PostgreSQL kullanılacaktır.
- SQLite production ortamında kullanılmayacaktır.
- Django ORM tercih edilir.
- Raw SQL yalnızca zorunlu durumlarda kullanılabilir.

---

## Docker

Docker Compose production amacıyla kullanılmaz.

Production için

- Docker
- Nginx
- Gunicorn
- PostgreSQL

kullanılır.

---

## Nginx

- HTTPS zorunludur.
- Gzip aktif olmalıdır.
- Security Header'ları aktif olmalıdır.
- Static dosyalar Nginx tarafından sunulmalıdır.

---

## Güvenlik

Deployment öncesinde aşağıdaki kontroller yapılmalıdır.

python manage.py check --deploy

python manage.py check

---

## Loglama

DEBUG çıktıları production ortamında kapalı olmalıdır.

Hatalar log dosyalarına yazılmalıdır.

---

## Backup

Deployment öncesinde PostgreSQL yedeği alınmalıdır.

Rollback planı hazırlanmalıdır.

---

## Performans

Deployment sonrasında aşağıdakiler kontrol edilmelidir.

- Response Time
- Database Query Count
- Static File Cache
- Gzip
- Security Headers

---

## Yasaklar

- DEBUG=True
- Hardcoded Secret Key
- Hardcoded Password
- Migration silmek
- Production veritabanında manuel değişiklik
- Git dışında deployment