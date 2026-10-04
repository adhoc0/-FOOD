---
title: Accounts Modülü
tags:
  - app-module
  - accounts
  - user-management
  - auth
date: 2026-09-28
---

# 👤 Accounts Modülü (`accounts/`)

Accounts modülü, platformdaki kullanıcı kimlik doğrulama, yetkilendirme, profil yönetimi ve kullanıcı ilişkilerinden sorumludur.

---

## 📐 Modeller (Models)

### `User` (`accounts.models.User`)
- Django'nun `AbstractUser` sınıfından türetilmiş özel kullanıcı modelidir.
- **Alanlar:**
  - `email` (EmailField, unique=True)
  - `username` (CharField, unique=True)
  - `bio` (TextField, optional)
  - `avatar` (ImageField, optional)
  - `is_verified` (BooleanField, default=False)
  - `created_at`, `updated_at`

---

## 🏛️ Mimari Katmanlar

### Services (`accounts/services/`)
- `user_service.py`: Kullanıcı kaydı (`register_user`), profil güncelleme (`update_profile`), şifre değiştirme.
- Tüm şifre güncellemeleri ve profil bilgisi değişiklikleri bu servis üzerinden yapılır.

### Selectors (`accounts/selectors/`)
- `user_selector.py`: `get_user_by_id`, `get_user_by_email`, `get_active_authors`.

### Validators (`accounts/validators/`)
- `user_validator.py`: Parola karmaşıklık kontrolü, avatar görsel boyutu ve format doğrulaması.

---

## 🔒 Yetkilendirme Matrisi

| Rol | Yetkiler |
| :--- | :--- |
| **Anonim Kullanıcı** | Tarif ve içerik görüntüleme |
| **Kayıtlı Kullanıcı** | Favori ekleme, puan verme, yorum yazma, kendi profilini güncelleme |
| **Yönetici (Admin)** | Yorum onaylama, içerik moderasyonu, kullanıcı yönetimi |

---

## 🔗 İlgili Bağlantılar
- [[Clean Architecture]] — Katman mimarisi
- [[Interactions Modülü]] — Kullanıcının favori, puan ve yorum ilişkileri
- [[Güvenlik Rehberi]] — Auth güvenliği standartları
