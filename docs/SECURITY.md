````md
# SECURITY

## Amaç

Bu doküman projenin güvenlik standartlarını, politikalarını ve uygulanması zorunlu kuralları tanımlar.

Güvenlik hiçbir zaman sonradan eklenen bir özellik değildir.

Projenin her katmanında güvenlik önceliklidir.

---

# Güvenlik Prensipleri

Her geliştirme aşağıdaki öncelik sırasına göre değerlendirilmelidir.

1. Veri Gizliliği
2. Veri Bütünlüğü
3. Yetkilendirme
4. Kimlik Doğrulama
5. Güvenli Kod
6. Güvenli Deployment
7. Güvenli Loglama

---

# Kimlik Doğrulama

Django Authentication sistemi kullanılacaktır.

Parolalar hiçbir zaman düz metin olarak saklanmaz.

Parolalar yalnızca Django'nun güvenli parola algoritmaları ile hashlenir.

Parolalar okunamaz.

---

# Yetkilendirme

Her işlem yetki kontrolünden geçmelidir.

Kullanıcı yalnızca kendi verisini değiştirebilir.

Admin yetkileri yalnızca gerekli kullanıcılara verilir.

Superuser hesabı günlük kullanım için kullanılmaz.

---

# Kullanıcı Rolleri

Anonim Kullanıcı

- Tarif görüntüleyebilir.

Kayıtlı Kullanıcı

- Favorilere ekleyebilir.
- Yorum yapabilir.
- Puan verebilir.
- Profilini düzenleyebilir.

Yönetici

- İçerik yönetebilir.
- Yorum onaylayabilir.
- Kullanıcı yönetebilir.

---

# Şifre Politikası

Minimum 12 karakter.

Büyük harf.

Küçük harf.

Rakam.

Özel karakter.

Zayıf parola kabul edilmez.

---

# CSRF

CSRF koruması kapatılmaz.

Tüm POST istekleri CSRF korumasından geçmelidir.

---

# XSS

Kullanıcı girdileri güvenli şekilde gösterilmelidir.

HTML çıktıları escape edilmelidir.

JavaScript içerisine doğrudan kullanıcı verisi yazılmaz.

innerHTML yerine mümkün olduğunca textContent kullanılmalıdır.

---

# SQL Injection

Raw SQL kullanılmaz.

Django ORM kullanılacaktır.

Parametreli sorgular kullanılacaktır.

Kullanıcı girdileri doğrudan sorguya eklenmez.

---

# Dosya Yükleme

Dosya türü doğrulanmalıdır.

Dosya boyutu sınırlandırılmalıdır.

Dosya uzantısı kontrol edilmelidir.

MIME Type doğrulanmalıdır.

Rastgele dosya adı oluşturulmalıdır.

Çalıştırılabilir dosyalar kabul edilmez.

---

# Görseller

Yalnızca güvenli görsel formatları kabul edilir.

Örnek

- jpg
- jpeg
- png
- webp

SVG yalnızca doğrulanmış içeriklerde kullanılmalıdır.

---

# Session Güvenliği

SESSION_COOKIE_SECURE=True

SESSION_COOKIE_HTTPONLY=True

SESSION_EXPIRE_AT_BROWSER_CLOSE=True

SESSION_COOKIE_SAMESITE="Lax"

---

# Cookie Güvenliği

CSRF_COOKIE_SECURE=True

CSRF_COOKIE_HTTPONLY=False

CSRF_COOKIE_SAMESITE="Lax"

---

# HTTPS

Production ortamında HTTPS zorunludur.

HTTP otomatik HTTPS'e yönlendirilmelidir.

TLS 1.2 veya üzeri kullanılmalıdır.

---

# Security Headers

Production ortamında aşağıdaki başlıklar aktif olmalıdır.

- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
- Permissions-Policy
- Strict-Transport-Security
- Content-Security-Policy

---

# Content Security Policy

Inline JavaScript kullanılmaz.

Inline CSS kullanılmaz.

Harici kaynaklar sınırlandırılır.

Sadece güvenilir alan adlarına izin verilir.

---

# Clickjacking

X-Frame-Options aktif olacaktır.

Site iframe içerisinde çalıştırılmaz.

---

# Rate Limiting

Login

Şifre sıfırlama

Yorum

Favori

API

işlemlerinde hız sınırı uygulanmalıdır.

---

# Brute Force Koruması

Başarısız giriş denemeleri sınırlandırılır.

Belirli sayıda başarısız denemeden sonra geçici engelleme uygulanır.

---

# Spam Koruması

Yorumlarda spam kontrolü yapılmalıdır.

Arka arkaya çok fazla istek engellenmelidir.

Bot davranışları tespit edilmelidir.

---

# Input Validation

Tüm kullanıcı girdileri doğrulanmalıdır.

Uzunluk kontrolü yapılmalıdır.

Karakter kontrolü yapılmalıdır.

Boş veri kontrolü yapılmalıdır.

---

# Output Escaping

Kullanıcıdan gelen veri doğrudan HTML içerisine yazılmaz.

Template filtreleri kullanılmalıdır.

---

# Logging

Loglara aşağıdakiler yazılmaz.

Parola

Token

Session ID

Cookie

Kart bilgisi

E-posta doğrulama kodu

API anahtarı

---

# Hata Mesajları

Production ortamında ayrıntılı hata gösterilmez.

Stack Trace kullanıcıya gösterilmez.

DEBUG=False kullanılacaktır.

---

# Ortam Değişkenleri

Aşağıdaki bilgiler yalnızca .env dosyasında tutulur.

SECRET_KEY

DATABASE_URL

EMAIL_PASSWORD

API_KEY

SECRET

TOKEN

JWT_SECRET

Hiçbiri Git deposuna eklenmez.

---

# Admin Paneli

Admin URL'si varsayılan bırakılmaz.

Admin hesabında güçlü parola zorunludur.

İki faktörlü doğrulama gelecekte desteklenecektir.

---

# Veritabanı

ORM kullanılacaktır.

Foreign Key kullanılacaktır.

Constraint kullanılacaktır.

Index kullanılacaktır.

SQL Injection'a karşı ORM tercih edilir.

---

# API Güvenliği

API geliştirildiğinde

Authentication zorunlu olacaktır.

Rate Limit uygulanacaktır.

Token doğrulaması yapılacaktır.

Versiyonlama kullanılacaktır.

---

# Üçüncü Parti Paketler

Yalnızca aktif olarak geliştirilen paketler kullanılmalıdır.

Düzenli güvenlik güncellemesi yapılmalıdır.

Kullanılmayan paketler kaldırılmalıdır.

---

# Dependency Yönetimi

Paketler düzenli güncellenmelidir.

Bilinen güvenlik açıkları takip edilmelidir.

---

# Backup Güvenliği

Yedekler şifrelenmelidir.

Farklı sunucuda saklanmalıdır.

Geri yükleme test edilmelidir.

---

# Deployment Güvenliği

DEBUG=False

HTTPS

Secure Cookies

Security Headers

Güncel işletim sistemi

Güncel Python

Güncel PostgreSQL

zorunludur.

---

# Güvenlik Testleri

Her sürüm öncesinde kontrol edilir.

- SQL Injection
- XSS
- CSRF
- File Upload
- Authentication
- Authorization
- Session
- Cookie
- Broken Links

---

# Güvenlik Olayları

Şüpheli girişler loglanmalıdır.

Başarısız giriş denemeleri kaydedilmelidir.

Yetkisiz erişim denemeleri raporlanmalıdır.

---

# Yasaklar

DEBUG=True ile production'a çıkmak.

SECRET_KEY'i Git'e eklemek.

.env dosyasını paylaşmak.

Parolaları düz metin saklamak.

Raw SQL kullanmak.

Inline JavaScript kullanmak.

Inline CSS kullanmak.

Kullanıcı girdisini doğrulamadan veritabanına kaydetmek.

Kullanıcı verisini escape etmeden HTML'e yazmak.

Loglara hassas bilgi yazmak.

Yetki kontrolü yapmadan işlem gerçekleştirmek.

Dosya yüklemelerinde uzantı kontrolü yapmamak.

HTTPS olmadan production ortamına çıkmak.

---

# Güvenlik Kontrol Listesi

Yayın öncesinde aşağıdaki maddelerin tamamı doğrulanmalıdır.

- DEBUG=False
- HTTPS aktif
- CSRF aktif
- XSS koruması aktif
- SQL Injection koruması aktif
- Güvenlik başlıkları aktif
- Güçlü parola politikası aktif
- Rate Limiting aktif
- Loglar kontrol edildi
- Backup alındı
- Ortam değişkenleri doğrulandı
- Hassas bilgiler Git deposunda bulunmuyor
- Bağımlılıklar güncel
- Güvenlik testleri başarıyla tamamlandı
```
````
