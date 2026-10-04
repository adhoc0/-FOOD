---
title: Pages ve Core Modülleri
tags:
  - app-module
  - pages
  - core
  - sitemap
date: 2026-09-28
---

# 📄 Pages ve Core Modülleri (`pages/` ve `core/`)

`pages` ve `core` modülleri, platformun açılış sayfalarını, statik içeriklerini (Hakkımızda, Gizlilik, İletişim), özel hata sayfalarını ve ortak middleware altyapısını barındırır.

---

## 🏛️ Ana Bileşenler

### 1. Statik Sayfalar (`pages/`)
- **Ana Sayfa (`HomeView`):** Öne çıkan tarifler, iller ve kategoriler.
- **Hakkımızda (`AboutView`):** Platform vizyonu ve misyonu.
- **Kullanım Şartları & Gizlilik (`TermsView`):** KVKK ve yasal metinler.
- Statik görünümler doğrudan ilgili Django şablonlarına bağlıdır, gereksiz ara katman içermez.

### 2. Güvenlik Middleware'i (`core/middleware.py`)
- `SecurityHeadersMiddleware`: CSP, HSTS, X-Frame-Options, Permissions-Policy başlıklarını otomatik enjekte eder ([[Güvenlik Rehberi]]).
- `RateLimitMiddleware`: İlgili hassas POST uçlarına istek sınırı koyar.

### 3. Dinamik Sitemap ve Robots.txt (`sitemaps/`)
- Django `sitemaps` modülü ile otomatik üretilen `sitemap.xml`:
  - `RecipeSitemap` (Tarifler)
  - `ProvinceSitemap` (İller)
  - `CategorySitemap` (Kategoriler)
  - `StaticViewSitemap` (Statik sayfalar)

---

## 🔗 İlgili Bağlantılar
- [[SEO ve Performans]] — Dynamic Sitemap ve Robots.txt detayları
- [[Güvenlik Rehberi]] — SecurityHeadersMiddleware detayları
- [[Clean Architecture]] — View katmanının inceliği
