---
title: Proje Yol Haritası (Roadmap)
tags:
  - roadmap
  - planning
  - status
date: 2026-09-28
---

# 🗺️ Proje Yol Haritası (Roadmap)

**Mevcut Durum:** `v0.3.0 (alpha)`  
**Aşama:** Temel alan modelleri, güvenlik başlıkları, veri bütünlüğü kısıtları ve test altyapısı kuruluyor.  
**Yayın Durumu:** Production'a hazır değil.

---

## 🚦 Faz Geçişleri ve Görev Listesi

### 🟢 Faz 0: Durum Analizi ve Yapılandırma
- [x] Projenin mevcut durumunu mimari ve güvenlik açısından denetle
- [x] Gerçek sürümü `alpha` olarak işaretle
- [x] Dokümantasyonu ve mimari kararları güncellerle
- [x] Dinamik sitemap ile çakışan statik sitemap dosyasını kaldır
- [x] Atomik commit grubunu planla

### 🟢 Faz 1: Test ve Doğrulama Altyapısı
- [x] Ayrı test settings modülü (`config.settings.test`)
- [x] Docker tabanlı test PostgreSQL servisi (`docker-compose.test.yml`)
- [x] Bütün uygulama test klasörlerinin pytest tarafından toplanması
- [x] PostgreSQL üzerinde tüm unit ve entegrasyon testlerinin çalıştırılması
- [ ] Kritik kullanıcı ve veri bütünlüğü akışlarının test kapsamını tamamla

### 🟡 Faz 2: Güvenlik ve Veri Bütünlüğü (Aktif)
- [x] Rating puanı için servis doğrulaması ve PostgreSQL `CheckConstraint` (1-5 aralığı)
- [x] `RecipeImage` model ve service girişlerinde görsel boyutu, uzantı ve magic-byte doğrulaması
- [x] Hassas POST uçları için cache tabanlı rate limiting middleware'i
- [x] CSP ve Permissions-Policy güvenlik başlıkları
- [x] Yetkilendirme matrisi ve kapsamlı permission testleri
- [x] Dependency ve secret taraması (`pip-audit`, Django 6.0.7 & Pillow 12.3.0 yükseltmesi)

### 🔵 Faz 3: Kullanıcı Arayüzü ve Akışlar (Gelecek)
- [ ] İl, kategori ve tarif liste/detay akışlarının tamamlanması
- [ ] Arama ve filtreleme mekanizması (PostgreSQL Full Text Search)
- [ ] Kullanıcı hesabı ve profil yönetimi akışları ([[Accounts Modülü]])
- [ ] Yorum moderasyonu ve bildirim altyapısı
- [ ] SEO, erişilebilirlik (WCAG 2.2 AA) ve performans doğrulamaları

### 🟣 Faz 4: Deployment ve Canlıya Alım
- [ ] Staging ortamında uçtan uca testler
- [ ] Production Nginx ve SSL sertifika kurulumu
- [ ] Otomatik günlük veritabanı yedekleme testi
- [ ] Health Check ve monitoring yapılandırması

---

## 🚫 Öncelik Kuralı
> [!IMPORTANT]
> Redis, Celery, REST API, çoklu dil desteği ve mobil uygulama geliştirmeleri; çekirdek ürün production kalitesine ulaşmadan kapsama alınmayacaktır.

---

## 🔗 İlgili Bağlantılar
- [[Proje Özeti]] — Proje vizyonu
- [[Değişiklik Günlüğü]] — Tamamlanan versiyon detayları
- [[Test Stratejisi]] — Test paketi yapılandırması
