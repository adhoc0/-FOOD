---
title: Recipes Modülü
tags:
  - app-module
  - recipes
  - food-data
  - schema-org
date: 2026-09-28
---

# 🍲 Recipes Modülü (`recipes/`)

Recipes modülü, platformun çekirdeğini oluşturan yöresel tariflerin, kategorilerin, mutfak türlerinin, malzemelerin ve etiketlerin yönetildiği modüldür.

---

## 📐 Modeller (Models)

### 1. `Recipe` (`recipes.models.Recipe`)
- Ana tarif modelidir.
- **Alanlar:**
  - `title` (CharField), `slug` (SlugField, unique=True, db_index=True)
  - `province` (ForeignKey -> [[Provinces Modülü#Province|Province]], on_delete=PROTECT)
  - `category` (ForeignKey -> `Category`, on_delete=PROTECT)
  - `cuisine` (ForeignKey -> `Cuisine`, on_delete=SET_NULL, null=True)
  - `prep_time_minutes` (PositiveIntegerField), `cook_time_minutes` (PositiveIntegerField)
  - `servings` (PositiveSmallIntegerField), `calories` (PositiveIntegerField, optional)
  - `instructions` (TextField), `summary` (TextField)
  - `is_featured` (BooleanField), `is_approved` (BooleanField)
  - `author` (ForeignKey -> [[Accounts Modülü#User|User]], on_delete=SET_NULL, null=True)

### 2. `Category` & `Cuisine` & `Tag`
- `Category`: Çorbalar, Kebaplar, Tatlılar vb.
- `Cuisine`: Saray Mutfağı, Yörük Mutfağı vb.
- `Tag`: #gaziantep, #fırın, #acılı.

### 3. `Ingredient` & `RecipeIngredient`
- Malzemeler normalize yapıda tutulur (`RecipeIngredient` ara tablosu miktar ve birim içerir).

### 4. `RecipeImage`
- Çoklu görsel desteği.
- [[Güvenlik Rehberi#4. Dosya Yükleme Güvenliği|RecipeImage Security]] uyarınca magic-byte ve 5MB sınırıyla yüklenir.

---

## 🏛️ Mimari Katmanlar

### Services (`recipes/services/`)
- `recipe_service.py`: `create_recipe(...)`, `update_recipe(...)`, `publish_recipe(...)`.
- `recipe_image_service.py`: Sıkıştırma, WebP dönüştürme ve güvenli kayıt.

### Selectors (`recipes/selectors/`)
- `recipe_selector.py`:
  - `get_featured_recipes()`
  - `get_recipes_by_province(province_slug)`
  - `get_recipe_detail_by_slug(slug)` (`select_related('province', 'category', 'author')` ve `prefetch_related('ingredients', 'images')` ile N+1 korumalı).

### Validators (`recipes/validators/`)
- `recipe_validator.py`: Sürelerin pozitifliği, zorunlu alanlar, görsel format ve boyut denetimleri.

---

## 🔗 İlgili Bağlantılar
- [[Provinces Modülü]] — Tariflerin il ve bölge bağlamı
- [[Interactions Modülü]] — Tarife verilen puan, favori ve yorumlar
- [[SEO ve Performans]] — Recipe Schema (JSON-LD) yapısı
- [[Güvenlik Rehberi]] — Görsel yükleme güvenlik doğrulaması
