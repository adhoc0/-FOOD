---
title: Değişiklik Günlüğü (Changelog)
tags:
  - changelog
  - releases
  - versioning
date: 2026-09-28
---

# 📜 Değişiklik Günlüğü (Changelog)

Proje [Semantic Versioning](https://semver.org/) (SemVer) standardını takip etmektedir.

---

## 🚀 [Unreleased] — Geliştirme Aşamasında

### 🛡️ Güvenlik ve Veri Bütünlüğü (Security & Data Integrity)
- **Django & Pillow Yükseltmesi:** `pip-audit` bulguları doğrultusunda Django 6.0.7 ve Pillow 12.3.0 güvenli sürümlerine yükseltildi.
- **Rating Constraint:** Puanlama 1-5 aralığına PostgreSQL `CheckConstraint` ve Service doğrulaması ile kısıtlandı.
- **RecipeImage Security:** Görsel yüklemelerine max 5MB boyut, uzantı ve magic-byte (görsel başlık imzası) doğrulaması eklendi.
- **Rate Limiting Middleware:** Hassas POST uçları için IP ve endpoint bazlı rate limiting aktif edildi.
- **Security Headers:** CSP ve Permissions-Policy başlıkları merkezi güvenlik middleware'ine bağlandı.

### 🏗️ Değiştirilenler (Changed)
- Proje sürümü `0.3.0 alpha` olarak işaretlendi.
- Statik sayfa view'ları doğrudan asıl şablonlara bağlandı.
- Test ayarları (`config.settings.test`) ve Docker test veritabanı ortamı güncellendi.
- Inline CSS kullanımı kaldırılarak CSP uyumu sağlandı.

### 🗑️ Kaldırılanlar (Removed)
- Dinamik sitemap endpoint'iyle çakışan statik `sitemap.xml` kaldırıldı.
- Kullanılmayan statik ara şablonlar ve `pages.views.views` modülü temizlendi.

---

## 📦 [0.3.0] - 2026-07-16 — Alpha Sürümü

### ➕ Eklenenler (Added)
- `accounts`, `provinces`, `recipes`, `pages`, `interactions` uygulamalarının temel yapıları.
- `Region`, `Province`, `Recipe`, `Category`, `Cuisine`, `Ingredient`, `Tag`, `Favorite`, `Rating`, `Comment` modelleri.
- Service, Selector, Validator katmanlarının başlangıç uygulamaları.
- Docker, Gunicorn, Nginx ve PostgreSQL geliştirme yapılandırması.

---

## 🔗 İlgili Bağlantılar
- [[Yol Haritası (Roadmap)]] — Planlanan gelecek sürümler
- [[Güvenlik Rehberi]] — Uygulanan güvenlik standartları
