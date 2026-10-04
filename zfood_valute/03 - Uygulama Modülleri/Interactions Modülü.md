---
title: Interactions Modülü
tags:
  - app-module
  - interactions
  - ratings
  - comments
  - favorites
date: 2026-09-28
---

# 💬 Interactions Modülü (`interactions/`)

Interactions modülü; kullanıcıların tariflere verdiği puanları, favori kayıtlarını ve yapılan yorumların moderasyon süreçlerini yönetir.

---

## 📐 Modeller ve Kısıtlar (Models & Constraints)

### 1. `Favorite` (`interactions.models.Favorite`)
- Kullanıcının favori tarif listesidir.
- **Kısıt:** `UniqueConstraint(fields=['user', 'recipe'])` — Bir kullanıcı aynı tarifi sadece 1 kez favoriye ekleyebilir.

### 2. `Rating` (`interactions.models.Rating`)
- Tarife verilen 1 ile 5 arasındaki derecelendirme puanıdır.
- **Kısıtlar:**
  - `UniqueConstraint(fields=['user', 'recipe'])` — Bir kullanıcı aynı tarife sadece 1 kez puan verebilir.
  - `CheckConstraint(check=Q(score__gte=1, score__lte=5))` — Puan veritabanı seviyesinde **1-5 arasında kalmak zorundadır**.

### 3. `Comment` (`interactions.models.Comment`)
- Tarif altındaki yorumlardır.
- **Alanlar:** `user`, `recipe`, `content`, `is_approved` (default=False), `created_at`.
- Admin onayı olmadan sitede yayınlanmaz.

---

## 🏛️ Mimari Katmanlar

### Services (`interactions/services/`)
- `rating_service.py`: `rate_recipe(user, recipe, score)` — Puan 1-5 aralığında değilse `ValidationError` fırlatır, başarılı ise tarif ortalamasını re-calculate eder.
- `favorite_service.py`: `toggle_favorite(user, recipe)`.
- `comment_service.py`: `add_comment(user, recipe, content)`, `approve_comment(comment_id)`.

### Selectors (`interactions/selectors/`)
- `rating_selector.py`: `get_recipe_average_rating(recipe_id)`.
- `comment_selector.py`: `get_approved_comments_for_recipe(recipe_id)`.

---

## 🔗 İlgili Bağlantılar
- [[Recipes Modülü]] — Puanlanan ve yorum yapılan tarifler
- [[Accounts Modülü]] — Yorum yapan kullanıcı ilişkileri
- [[Güvenlik Rehberi]] — Yorum uçlarında rate limiting
