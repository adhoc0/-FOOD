---
title: Proje Özeti ve Vizyonu
tags:
  - general
  - overview
  - tech-stack
date: 2026-09-28
---
# 📖 Proje Özeti ve Vizyonu

**FOOD Projesi**, Türkiye'nin tüm yöresel yemeklerini tek bir çatı altında toplayan, her ilin gastronomi kültürünü en doğru verilerle tanıtan, yüksek performanslı, güvenli ve SEO odaklı bir web platformudur.

Bu proje basit bir tarif paylaşım sitesi değildir; kurumsal standartlarda geliştirilen, yüz binlerce kullanıcıyı ve on binlerce tarifi destekleyecek şekilde ölçeklenebilir bir gastronomi altyapısıdır.

---

## 🎯 Projenin Temel Amaçları

1. **Yöresel Gastronomi Arşivi:** Türkiye'nin 81 ilinin özgün yemeklerini, tariflerini ve malzemelerini tam doğrulukla kayıt altına almak.
2. **SEO Liderliği:** Yemek ve tarif aramalarında Türkiye'nin en güçlü arama motoru görünürlüğüne sahip olmak ([[SEO ve Performans]]).
3. **Sürdürülebilir Mimari:** Clean Architecture prensiplerine tam uyum sağlayarak uzun yıllar bakım yapılabilir bir altyapı korumak ([[Clean Architecture]]).
4. **Üst Düzey Kullanıcı Deneyimi:** Hızlı yüklenen, mobil uyumlu, minimalist ve erişilebilir bir arayüz sunmak.

---

## 🛠️ Teknoloji Yığını (Tech Stack)

### Backend
- **Dil:** Python 3.14+
- **Framework:** Django 6.0+
- **Veritabanı:** PostgreSQL 16+ (UTF-8, UTC)
- **Mimari Desen:** Clean Architecture (Services, Selectors, Validators, Models)

### Frontend
- **HTML:** Semantic HTML5, WAI-ARIA erişilebilirlik
- **CSS:** Vanilla CSS3 (Component tabanlı, BEM benzeri modüler yapı)
- **JavaScript:** Vanilla JS (ES6+ Modüler, Fetch API, zero-dependency)

### Infrastructure & Deployment
- **Containerization:** Docker & Docker Compose
- **WSGI Application Server:** Gunicorn
- **Web Sunucusu & Reverse Proxy:** Nginx (Gzip, HTTPS, static/media sunumu)

### Gelecek Fazlar
- **Caching:** Redis
- **Arka Plan Görevleri:** Celery
- **Arama Motoru:** PostgreSQL Full Text Search -> Elasticsearch

---

## 🔗 İlgili Bağlantılar
- [[Clean Architecture]] — Mimari katmanların detayları
- [[Yol Haritası (Roadmap)]] — Mevcut geliştirme aşaması
- [[Güvenlik Rehberi]] — Güvenlik kuralları ve standartları
- [[Veritabanı Mimarisi]] — PostgreSQL şema kuralları
