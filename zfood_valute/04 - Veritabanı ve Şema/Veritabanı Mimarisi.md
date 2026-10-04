---
title: Veritabanı Mimarisi ve Kuralları
tags:
  - database
  - postgresql
  - schema
  - indexes
date: 2026-09-28
---

# 🗄️ Veritabanı Mimarisi ve Kuralları

FOOD projesinin veritabanı altyapısı **PostgreSQL 16** üzerine kurulu, tamamen normalize edilmiş, yüksek veri bütünlüğü sağlayan bir yapıya sahiptir.

---

## ⚙️ Temel Veritabanı Ayarları
- **Veritabanı Motoru:** PostgreSQL 16+
- **Karakter Seti (Encoding):** UTF-8
- **Zaman Dilimi:** UTC
- **Primary Key Tipi:** `BigAutoField` (Otomatik artan 64-bit integer)

---

## 📜 Veritabanı Tasarım Standartları

### 1. Tablo ve Alan İsimlendirmeleri
- **Tablo İsimleri:** Tekil (`snake_case`) olmalıdır (Örn: `recipe`, `province`, `user_profile`). Çoğul tablo ismi (`recipes`) **kullanılmaz**.
- **Alan İsimleri:** `snake_case` (Örn: `created_at`, `updated_at`, `plate_code`).
- **Foreign Key Alanları:** Doğrudan hedef model adıyla tanımlanır (Örn: `province`, `category`, `author`).

### 2. İndeks Stratejisi (Indexes)
Performansı korumak adına aşağıdaki alanlarda indeks kullanımı zorunludur:
- Tüm `SlugField` alanları (`unique=True, db_index=True`)
- `plate_code` (İl plaka kodu)
- Foreign Key ilişkileri
- Sık sorgulanan zaman alanları (`created_at`)

### 3. Kısıtlar (Constraints)
- **Unique Constraint:** Mükerrer kayıt engelleme (`Favorite(user, recipe)`, `Rating(user, recipe)`, `Province(plate_code)`).
- **Check Constraint:** Mantıksal veri sınırları (`Rating(score >= 1 AND score <= 5)`).

### 4. Foreign Key Silme Davranışları (Delete Cascade Policy)
- Varsayılan olarak bilinçsiz `CASCADE` **kullanılmaz**.
- `Region` -> `Province`: `PROTECT` (Bölge silinemez).
- `Province` -> `Recipe`: `PROTECT` (İlişkili ili olan tarif silinirken il korunur).
- `Category` -> `Recipe`: `PROTECT`.
- `User` -> `Recipe`: `SET_NULL` (Yazar hesabı silinirse tarif anonim kalır).

---

## 🚫 Veritabanı Yasakları
- ❌ **Soft Delete Kullanmak:** Silinen veriler veritabanından tamamen temizlenir veya arşiv tablosuna aktarılır; `is_deleted` bayrağı ile biriktirilmez.
- ❌ **Float Kullanmak:** Ortalama puan veya maliyet için `Float` yerine `DecimalField` kullanılır.
- ❌ **Veritabanında Dosya Saklamak:** Görselin/dosyanın kendisi veritabanında saklanmaz, sadece dosya yolu (`MEDIA_ROOT` bağıntılı) tutulur.
- ❌ **Manuel Migration Düzenlemek:** Oluşturulmuş Django migration dosyaları elle değiştirilmez, yeni migration üretilir.

---

## 🔗 İlgili Bağlantılar
- [[Veri Modelleri ERD]] — Modeller arası ilişki şeması
- [[Clean Architecture]] — Selector ve ORM katmanı kuralları
- [[Interactions Modülü]] — Rating CheckConstraint kuralı
