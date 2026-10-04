---
title: Provinces Modülü
tags:
  - app-module
  - provinces
  - geography
  - regions
date: 2026-09-28
---

# 🗺️ Provinces Modülü (`provinces/`)

Provinces modülü, Türkiye'nin coğrafi bölgelerini ve 81 ilini temsil eden, platformun gastronomi haritasının temel referans katmanıdır.

---

## 📐 Modeller (Models)

### 1. `Region` (`provinces.models.Region`)
- Türkiye'nin 7 coğrafi bölgesini temsil eder (Güneydoğu Anadolu, Ege, İç Anadolu vb.).
- **Alanlar:** `name`, `slug`, `is_active`, `created_at`.
- > [!IMPORTANT]
  > [[Mimari Kararlar (ADR)#ADR-001|ADR-001]] uyarınca `Region` kayıtları fiziksel olarak silinmez, sadece `is_active=False` yapılır.

### 2. `Province` (`provinces.models.Province`)
- Türkiye'nin 81 ilini temsil eder (Gaziantep, Konya, Hatay vb.).
- **Alanlar:**
  - `name` (CharField, unique=True)
  - `plate_code` (PositiveSmallIntegerField, unique=True, db_index=True)
  - `region` (ForeignKey -> Region, on_delete=PROTECT)
  - `slug` (SlugField, unique=True)
  - `description` (TextField)
  - `image` (ImageField)
  - `is_active` (BooleanField, default=True)

---

## 🏛️ Mimari Katmanlar

### Selectors (`provinces/selectors/`)
- `province_selector.py`:
  - `get_active_provinces()`
  - `get_province_by_slug(slug)`
  - `get_provinces_by_region(region_slug)`
  - `get_provinces_with_recipe_count()` (Annotate edilmiş tarif sayıları ile)

---

## 🔗 İlgili Bağlantılar
- [[Recipes Modülü]] — İllere bağlı yöresel tarifler
- [[Mimari Kararlar (ADR)]] — ADR-001 Bölge silmeme kararı
- [[Veritabanı Mimarisi]] — Plaka kodu ve slug indeksleri
