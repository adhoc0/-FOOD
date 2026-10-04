---
title: Kodlama Standartları ve Kuralları
tags:
  - coding-standards
  - pep8
  - clean-code
date: 2026-09-28
---

# 📝 Kodlama Standartları ve Kuralları

FOOD projesinde yazılan her satır kod okunabilir, test edilebilir, bakımı kolay ve sürdürülebilir olmak zorundadır.

---

## 🔤 İsimlendirme Kuralları (Naming Conventions)

| Yapı | Stil | Örnek |
| :--- | :--- | :--- |
| **Sınıflar (Classes)** | `PascalCase` | `RecipeService`, `ProvinceSelector`, `RecipeImage` |
| **Fonksiyonlar & Metotlar** | `snake_case` | `calculate_average_rating()`, `get_popular_recipes()` |
| **Değişkenler** | `snake_case` | `recipe_slug`, `active_province_list` |
| **Sabitler (Constants)** | `UPPER_CASE` | `MAX_IMAGE_SIZE_BYTES`, `DEFAULT_PAGE_SIZE` |
| **Dosya İsimleri** | `snake_case` | `recipe_service.py`, `image_validator.py` |

---

## 🐍 Python & Django Kuralları

1. **PEP8 Standartları:** Maksimum satır uzunluğu **120 karakterdir**.
2. **Import Sırası:**
   - 1. Standard Library (`os`, `sys`, `typing`)
   - 2. Django (`django.db`, `django.http`)
   - 3. Third-party packages (`PIL`, `pytest`)
   - 4. Local App modules (`apps.recipes...`)
3. **Wildcard Import Yasaktır:** `from module import *` kullanımı kesinlikle yasaktır.
4. **Tip Belirteçleri (Type Hints):** Service ve Selector fonksiyonlarında type hint kullanımı önerilir.
5. **Yorum Satırları:** Yorumlar kodun "ne yaptığını" değil, "neden yapıldığını" açıklamalıdır.

---

## 🚫 Kesinlikle Yasak Olan Uygulamalar

- ❌ **Magic Numbers:** Kod içerisinde açıklanmayan ham sayılar kullanmak (`if status == 3:` yerine `if status == RecipeStatus.PUBLISHED:`).
- ❌ **Hardcoded Stringler:** URL veya ayar değerlerini kod içine gömmek.
- ❌ **Sessiz Hata Yakalama:** `except: pass` veya `except Exception: pass` yazmak.
- ❌ **Tek Harfli Değişkenler:** `i`, `x`, `tmp` gibi anlamsız değişken isimleri.
- ❌ **Raw SQL:** Zorunlu haller dışında Django ORM harici ham SQL çalıştırmak.
- ❌ **Inline CSS ve JS:** HTML içerisinde `style="..."` veya `<script>` yazmak.

---

## 🔗 İlgili Bağlantılar
- [[Clean Architecture]] — Katman mimarisi ve görev dağılımları
- [[Güvenlik Rehberi]] — Güvenli kod yazma ilkeleri
- [[Veritabanı Mimarisi]] — PostgreSQL ORM standartları
