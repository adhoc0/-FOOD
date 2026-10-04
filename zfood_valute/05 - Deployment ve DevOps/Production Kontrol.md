---
title: Production Kontrol Listesi (Pre-Launch Checklist)
tags:
  - devops
  - production
  - checklist
  - security
date: 2026-09-28
---

# ✅ Production Kontrol Listesi (Pre-Launch Checklist)

Canlı ortama (Production) çıkış yapmadan önce aşağıdaki tüm maddeler eksiksiz olarak doğrulanmak zorundadır.

---

## 🔒 Güvenlik ve Ayarlar
- [ ] `DEBUG = False` yapıldı.
- [ ] `SECRET_KEY` ortam değişkeninden okunuyor ve rastgele en az 50 karakterlik karmaşık anahtar.
- [ ] `ALLOWED_HOSTS` sadece production alan adlarını içeriyor.
- [ ] `SECURE_SSL_REDIRECT = True` aktif.
- [ ] `SESSION_COOKIE_SECURE = True` ve `CSRF_COOKIE_SECURE = True` ayarlandı.
- [ ] [[Güvenlik Rehberi#Güvenlik Başlıkları (Security Headers)|Security Headers]] (CSP, HSTS, X-Frame-Options) aktif.

---

## 🗄️ Veritabanı ve Medya
- [ ] Veritabanı migration'ları sorunsuz uygulandı (`python manage.py migrate`).
- [ ] Otomatik günlük veritabanı yedekleme cron'u kuruldu ve test edildi.
- [ ] `collectstatic` komutu çalıştırıldı (`python manage.py collectstatic --noinput`).
- [ ] Nginx static ve media izinleri doğrulandı.

---

## 🩺 Sağlık ve Performans (Health Check)
- [ ] Sunucu ve container'lar sorunsuz yeniden başlıyor.
- [ ] Nginx Gzip sıkıştırması aktif.
- [ ] Log rotation (Error log, Access log) konfigüre edildi.
- [ ] Google Search Console ve Analytics bağlantıları tanımlandı.
- [ ] Lighthouse skorları (Performance > 90, Accessibility > 90, SEO = 100) doğrulandı.

---

## 🔗 İlgili Bağlantılar
- [[Docker ve Nginx]] — Container deployment adımları
- [[Güvenlik Rehberi]] — Güvenlik detayları
- [[Yol Haritası (Roadmap)]] — Faz 4 yayın hedefleri
