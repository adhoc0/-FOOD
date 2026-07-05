# ARCHITECTURE

## 1. Proje Amacı

Projenin teknik amacı.

---

## 2. Yazılım Prensipleri

- Clean Architecture
- SOLID
- DRY
- KISS
- YAGNI
- Single Responsibility
- Explicit is better than implicit

---

## 3. Teknolojiler

Python

Django

PostgreSQL

HTML

CSS

JavaScript

Docker

Nginx

Gunicorn

Redis (gelecekte)

Celery (gelecekte)

---

## 4. Klasör Yapısı

Tüm klasörlerin görevleri.

---

## 5. Django App Kuralları

Her uygulama yalnızca kendi iş mantığından sorumludur.

App'ler birbirlerinin modellerini doğrudan yönetemez.

Business Logic yalnızca Service katmanında bulunur.

Selector katmanı yalnızca veri okur.

Validator katmanı yalnızca doğrulama yapar.

View katmanı yalnızca HTTP işlemlerini yönetir.

---

## 6. Models Kuralları

Modeller yalnızca veri tanımlar.

İş mantığı model içerisinde yazılmaz.

ForeignKey ilişkileri açık şekilde tanımlanır.

ManyToMany gerektiğinde ara tablo kullanılır.

Delete davranışları bilinçli seçilir.

---

## 7. Services Kuralları

İş mantığı burada bulunur.

View içerisinde iş mantığı yazılmaz.

---

## 8. Selectors Kuralları

Tüm karmaşık sorgular burada bulunur.

View içinde queryset oluşturulmaz.

---

## 9. Validators Kuralları

Tüm doğrulamalar burada bulunur.

---

## 10. Signals Kuralları

Sadece otomatik işlemler.

İş mantığı yazılmaz.

---

## 11. Admin Kuralları

Her model için ayrı admin dosyası.

Admin paneli performanslı olmalıdır.

N+1 sorgularına izin verilmez.

---

## 12. URL Kuralları

REST benzeri yapı.

Slug kullanılmalıdır.

Anlamsız URL kullanılmaz.

---

## 13. HTML Kuralları

Component tabanlı.

Tekrar eden kod yasaktır.

Semantic HTML zorunludur.

Accessibility zorunludur.

---

## 14. CSS Kuralları

Component bazlı.

Sayfa bazlı.

Global CSS minimum.

Magic Number kullanılmaz.

!important yasaktır.

---

## 15. JavaScript Kuralları

Modüler yapı.

Global değişken yasaktır.

Inline JavaScript yasaktır.

Fetch API kullanılacaktır.

---

## 16. Veritabanı Kuralları

Normalize yapı.

Index kullanımı.

Unique Constraint.

Check Constraint.

Transaction kullanımı.

---

## 17. Güvenlik Kuralları

CSRF

XSS

SQL Injection

Clickjacking

Rate Limit

Password Hashing

Input Validation

Output Escaping

---

## 18. Performans Kuralları

select_related()

prefetch_related()

Pagination

Cache

Image Optimization

Static Compression

---

## 19. SEO Kuralları

Unique Title

Unique Description

Canonical

OpenGraph

Twitter Card

JSON-LD

Breadcrumb

---

## 20. Test Kuralları

Model Testleri

View Testleri

Service Testleri

Selector Testleri

Validator Testleri

---

## 21. Logging

Error Log

Access Log

Security Log

Audit Log

---

## 22. Deployment

Docker

Gunicorn

Nginx

HTTPS

Backup

Monitoring

---

## 23. Kod Yazma Kuralları

Kod okunabilir olmalıdır.

Kısa isim kullanılmaz.

Tek harfli değişken kullanılmaz.

Fonksiyonlar tek sorumluluğa sahip olmalıdır.

Kod tekrarına izin verilmez.

Yorum satırları kodu açıklamak için değil, neden yazıldığını açıklamak için kullanılmalıdır.

---

## 24. Yasaklar

View içinde Business Logic yazmak.

Raw SQL kullanmak (zorunlu olmadıkça).

Tekrar eden kod yazmak.

Magic Number kullanmak.

Hardcoded değer kullanmak.

Inline CSS.

Inline JavaScript.

Kopyala-yapıştır kod.

Performansı düşüren sorgular.

Test edilmemiş kod.

Dokümantasyonsuz yeni özellik eklemek.

---

## 25. Geliştirme Süreci

1. ROADMAP güncellenir.
2. ARCHITECTURE kontrol edilir.
3. Gerekirse mimari kararı dokümante edilir.
4. Model tasarlanır.
5. Servis yazılır.
6. Selector yazılır.
7. Validator yazılır.
8. View yazılır.
9. Template yazılır.
10. CSS yazılır.
11. JavaScript yazılır.
12. Test yazılır.
13. Kod gözden geçirilir.
14. Performans kontrol edilir.
15. Güvenlik kontrol edilir.
16. Commit atılır.