---
title: Mimari Karar Kayıtları (Architectural Decision Records)
tags:
  - adr
  - decisions
  - architecture
date: 2026-09-28
---

# 🏛️ Mimari Karar Kayıtları (ADR)

Bu doküman, projenin mimarisi ve veri bütünlüğü ile ilgili alınan kritik teknik kararları gerekçeleriyle kaydeder.

---

## 📌 ADR-001: Region Modeli Kayıtlarının Fiziksel Olarak Silinmemesi

### Karar
`Region` (Coğrafi Bölge) kayıtları veritabanından fiziksel olarak `DELETE` sorgusu ile silinmeyecektir. Bir bölge pasife alınmak istendiğinde yalnızca `is_active = False` bayrağı güncellenecektir.

### Gerekçe
`Region` modeli; `Province` (İller) ve `Recipe` (Tarifler) modellerinin temel üst referans tablosudur. Bir bölge kaydının silinmesi, ona bağlı onlarca ilin ve yüzlerce tarifin veri bütünlüğünü ve Foreign Key bağını riske atar.

### Sonuç
- `Province.region` ForeignKey ilişkisi `on_delete=models.PROTECT` olarak tanımlanmıştır.
- Silme isteği geldiğinde `RegionService` sadece `is_active=False` yapar.

---

## 📌 ADR-002: Service / Selector / Validator Ayrımının Zorunlu Kılınması

### Karar
Django'nun varsayılan fat-model veya fat-view şablonunun aksine, tüm iş mantığı `Service`, tüm sorgular `Selector`, tüm kurallar `Validator` sınıflarına modüler olarak dağıtılacaktır.

### Gerekçe
Uzun vadeli geliştirilebilirliği korumak, birim testlerini (unit tests) veritabanına veya HTTP katmanına bağımlı olmadan izole çalıştırabilmek ve N+1 sorgu hatalarını engellemek.

### Sonuç
View katmanı 10-15 satırı geçmeyen ince bir HTTP yönlendiricisi olarak kalır.

---

## 🔗 İlgili Bağlantılar
- [[Clean Architecture]] — Mimari katman yapısı
- [[Provinces Modülü]] — Region ve Province modelleri
- [[Test Stratejisi]] — Test izolasyonu
