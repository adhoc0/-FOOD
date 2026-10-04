---
title: FOOD Projesi - Ana Sayfa (Map of Content)
tags:
  - moc
  - index
  - food-project
  - architecture
date: 2026-09-28
---
# 🍲 FOOD Projesi - Obsidian Bilgi Kasası (Vault)

Türkiye'nin en kaliteli, güvenilir, hızlı ve profesyonel **Yöresel Yemek Platformu** için hazırlanan merkezi bilgi kasasına hoş geldiniz.

Bu vault, projenin mimari kararlarını, veri modellerini, iş mantığı kurallarını, güvenlik politikalarını, SEO standartlarını ve modül detaylarını Obsidian'ın dinamik bağlantı (`[[WikiLink]]`) yapısıyla sunar.

---

## 🗺️ Ana Gezinti (Map of Content)

### 📌 1. Proje Genel Bilgileri
- [[Proje Özeti]] — Proje vizyonu, hedefleri ve teknoloji yığını
- [[Yol Haritası (Roadmap)]] — Aşamalı geliştirme planı ve aktif durum (v0.3.0 alpha)
- [[Değişiklik Günlüğü]] — Versiyon geçmişi ve tamamlanan geliştirmeler
- [[Eksikler Raporu]] — Kod ve doküman incelemesinden çıkan eksikler (2026-09-29)

### 🏛️ 2. Mimari ve Geliştirme Standartları
- [[Clean Architecture]] — Katmanlı mimari (Services, Selectors, Validators, Views)
- [[Kodlama Standartları]] — PEP8, isimlendirme kuralları ve kod kalitesi
- [[Güvenlik Rehberi]] — Auth, CSRF, XSS, Rate Limiting, CSP ve Dosya Doğrulama
- [[SEO ve Performans]] — Schema.org, Core Web Vitals, OpenGraph ve Sorgu Optimizasyonu

### 📦 3. Uygulama Modülleri (Django Apps)
- [[Accounts Modülü]] — Kullanıcı yönetimi, profil ve kimlik doğrulama
- [[Provinces Modülü]] — Coğrafi bölgeler, iller ve plaka kodları
- [[Recipes Modülü]] — Tarifler, kategoriler, mutfaklar, malzemeler ve görseller
- [[Interactions Modülü]] — Favoriler, puanlama (1-5 constraint) ve yorum moderasyonu
- [[Pages ve Core]] — Statik sayfalar, dinamik sitemap ve temel görünüm katmanı

### 🗄️ 4. Veritabanı ve Veri Modeli
- [[Veritabanı Mimarisi]] — PostgreSQL 16 standartları, indeksleme ve transaction yönetimi
- [[Veri Modelleri ERD]] — Modeller arası ilişkiler, Foreign Key kuralları ve Mermaid şeması

### 🚀 5. Deployment ve DevOps
- [[Docker ve Nginx]] — Container yapısı, Gunicorn ve Nginx reverse proxy
- [[Production Kontrol]] — Canlıya alım öncesi güvenlik ve yayın kontrol listesi

### 📝 6. Geliştirici Notları ve Süreçler
- [[Mimari Kararlar (ADR)]] — Alınan kritik mimari kararlar (ADR-001 vb.)
- [[Test Stratejisi]] — Pytest, PostgreSQL test veritabanı ve CI/CD hattı
- [[Obsidian Kullanım Rehberi]] — Bu kasadan maksimum verim alma rehberi

---

## 📐 Temel Yazılım Prensipleri

Projedeki tüm geliştirmelerde aşağıdaki prensipler **tavizsiz** uygulanır:

| Prensip | Açıklama |
| :--- | :--- |
| **Clean Architecture** | İş mantığı sadece [[Clean Architecture#Service Katmanı|Service]], veri okuma [[Clean Architecture#Selector Katmanı|Selector]], doğrulama [[Clean Architecture#Validator Katmanı|Validator]] katmanındadır. |
| **DRY / KISS / YAGNI** | Kod tekrarı yapılmaz, gereksiz karmaşıklıktan ve erken optimizasyondan kaçınılır. |
| **Sıfır Geçici Çözüm** | Hızlı yama veya geçici kod yazılmaz; her karar uzun vadeli ölçeklenebilirliği hedefler. |
| **Güvenlik Öncelikli** | Tüm yetkilendirme, veri doğrulama ve XSS/CSRF korumaları geliştirme anında eklenir ([[Güvenlik Rehberi]]). |
| **SEO Uyumlu** | Her halka açık sayfa Schema.org, OpenGraph ve performans standartlarını karşılar ([[SEO ve Performans]]). |

---

## 🏷️ Etiket İndeksi
- #architecture — Mimari ve katman kuralları
- #app-module — Django uygulama modülleri
- #database — PostgreSQL ve veri modeli
- #security — Güvenlik standartları ve doğrulama
- #seo — Arama motoru optimizasyonu
- #devops — Docker, Nginx ve yayın süreçleri
