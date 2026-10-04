---
title: Güvenlik Rehberi ve Standartları
tags:
  - security
  - authentication
  - headers
  - rate-limiting
date: 2026-09-28
---

# 🛡️ Güvenlik Rehberi ve Standartları

FOOD platformunda güvenlik sonradan eklenen bir bileşen değil, mimarinin temel taşıdır.

---

## 🔒 Temel Güvenlik Mekanizmaları

### 1. Kimlik Doğrulama ve Yetkilendirme (Auth & AuthZ)
- Django'nun dahili `AbstractUser` tabanlı kimlik doğrulama altyapısı kullanılır.
- Parolalar Django'nun PBKDF2 / Argon2 algoritmaları ile hash'lenir, asla düz metin saklanmaz.
- Her uç noktada yetki matrisi (`IsAuthenticated`, `IsOwnerOrReadOnly`) doğrulanır.

### 2. XSS ve Output Escaping
- Şablonlarda tüm veriler varsayılan olarak HTML escape edilir.
- `safe` filtresi veya `mark_safe` kullanımı güvenlik incelemesi olmadan yapılamaz.
- İstemci tarafında `innerHTML` yerine `textContent` kullanımı zorunludur.

### 3. CSRF Koruması
- Tüm state değiştiren (POST, PUT, DELETE) isteklerde CSRF token doğrulanır.
- `CSRF_COOKIE_HTTPONLY = False` (JS erişimi için), `CSRF_COOKIE_SAMESITE = 'Lax'`.

### 4. Dosya Yükleme Güvenliği (`RecipeImage`)
Görsel yüklemelerinde üç kademeli doğrulama uygulanır:
1. **Boyut Kontrolü:** Maksimum 5 MB.
2. **Uzantı Kontrolü:** Sadece `.jpg`, `.jpeg`, `.png`, `.webp`.
3. **Magic-Byte Doğrulaması:** Dosya başlık imzası (`Pillow` aracılığıyla) incelenerek Sahte/Zararlı içerikler engellenir.

---

## 🌐 Güvenlik Başlıkları (Security Headers)

`core.middleware.SecurityHeadersMiddleware` aracılığıyla aşağıdaki başlıklar tüm isteklere eklenir:

```http
Content-Security-Policy: default-src 'self'; img-src 'self' data: https:; style-src 'self'; script-src 'self';
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=(), camera=()
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

---

## ⏱️ Rate Limiting (Hız Sınırı)

Hassas POST ve kimlik doğrulama uç noktalarına IP ve Kullanıcı bazlı cache limitleri uygulanır:
- **Giriş / Parola Sıfırlama:** 5 istek / dakika
- **Yorum Yapma:** 3 istek / dakika
- **Favori / Puan Verme:** 10 istek / dakika

---

## 🚫 Güvenlik Yasakları
- ❌ Production ortamında `DEBUG = True` bırakmak.
- ❌ Gizli anahtarları (`SECRET_KEY`, şifreler) Git deposuna commit etmek.
- ❌ Raw SQL kullanarak SQL Injection riski oluşturmak.
- ❌ Inline JavaScript veya inline CSS yazmak.

---

## 🔗 İlgili Bağlantılar
- [[Clean Architecture]] — Katmanlı doğrulama mantığı
- [[Recipes Modülü]] — RecipeImage yükleme güvenliği
- [[Production Kontrol]] — Canlıya alım öncesi güvenlik listesi
