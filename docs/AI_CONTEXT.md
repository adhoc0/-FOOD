```md
# AI_CONTEXT.md

## Projenin Amacı

Bu proje Türkiye'nin en kaliteli, güvenilir, hızlı ve profesyonel yöresel yemek platformunu oluşturmak amacıyla geliştirilmektedir.

Bu proje yalnızca tarif paylaşım sitesi değildir.

Amaç;

- Türkiye'nin tüm yöresel yemeklerini tek platformda toplamak
- Her ilin gastronomi kültürünü tanıtmak
- SEO açısından Türkiye'nin en güçlü yemek sitesi olmak
- Uzun yıllar geliştirilebilecek sürdürülebilir bir altyapı oluşturmak
- Kurumsal kalite standartlarında yazılım geliştirmek

Bu proje hobi projesi değildir.

Her yazılan satır uzun vadeli düşünülmelidir.

---

# Yapay Zekanın Görevi

Yapay zekâ yalnızca kod yazan araç değildir.

Görevi;

- Yazılım mimarisini korumak
- Kod kalitesini artırmak
- Performansı artırmak
- Güvenliği artırmak
- Gereksiz kod yazılmasını engellemek
- Kod tekrarını önlemek
- Profesyonel standartları korumaktır.

---

# Geliştirme Felsefesi

Her zaman;

Doğruluk

Okunabilirlik

Bakım kolaylığı

Performans

Güvenlik

Ölçeklenebilirlik

önceliklidir.

Kısa çözümler yerine uzun vadeli çözümler tercih edilir.

---

# Yazılım Prensipleri

Her geliştirme aşağıdaki prensiplere uygun olmalıdır.

- Clean Architecture
- SOLID
- DRY
- KISS
- YAGNI
- Single Responsibility Principle
- Separation of Concerns
- Explicit is better than implicit

---

# Teknoloji Yığını

Backend

- Python
- Django
- PostgreSQL

Frontend

- HTML5
- CSS3
- JavaScript (Vanilla)

Deployment

- Docker
- Gunicorn
- Nginx

Gelecekte

- Redis
- Celery
- Elasticsearch

---

# Kod Yazma Kuralları

Kod okunabilir olmalıdır.

Kod kısa değil doğru olmalıdır.

Fonksiyonlar tek iş yapmalıdır.

Tek harfli değişken isimleri kullanılmaz.

Magic Number kullanılmaz.

Hardcoded değer kullanılmaz.

Kod tekrarına izin verilmez.

Her dosyanın tek sorumluluğu vardır.

Yorum satırları "ne yaptığını" değil "neden yapıldığını" açıklar.

---

# Django Kuralları

Business Logic View içerisinde yazılmaz.

Business Logic Model içerisinde yazılmaz.

Business Logic yalnızca Service katmanında bulunur.

Selector yalnızca veri okur.

Validator yalnızca doğrulama yapar.

Signal yalnızca otomatik işlemler içindir.

Admin yalnızca yönetim panelidir.

---

# Model Kuralları

Her model tek sorumluluğa sahiptir.

ForeignKey ilişkileri açık tanımlanmalıdır.

ManyToMany gerekiyorsa ara tablo kullanılmalıdır.

Veritabanı normalize edilmelidir.

Her tablo gerektiğinde index kullanmalıdır.

Constraint kullanılmalıdır.

---

# View Kuralları

View mümkün olduğunca küçük tutulmalıdır.

View yalnızca;

- Request alır
- Service çağırır
- Response döndürür

View içerisinde karmaşık sorgu yazılmaz.

View içerisinde Business Logic yazılmaz.

---

# Service Kuralları

İş kuralları burada bulunur.

Transaction gerekiyorsa burada yönetilir.

Birden fazla modeli ilgilendiren işlemler burada yapılır.

---

# Selector Kuralları

Karmaşık sorgular burada bulunur.

select_related kullanılmalıdır.

prefetch_related kullanılmalıdır.

N+1 sorgularına izin verilmez.

---

# Validator Kuralları

Tüm doğrulamalar Validator katmanında yapılır.

View doğrulama yapmaz.

---

# HTML Kuralları

Semantic HTML kullanılmalıdır.

Component yapısı korunmalıdır.

Tekrar eden HTML yazılmaz.

Accessibility desteklenmelidir.

---

# CSS Kuralları

Component bazlı geliştirme yapılacaktır.

Sayfa bazlı CSS kullanılacaktır.

Global CSS minimum seviyede tutulacaktır.

!important kullanılmayacaktır.

Magic Number kullanılmayacaktır.

Responsive tasarım zorunludur.

---

# JavaScript Kuralları

Vanilla JavaScript kullanılacaktır.

Inline JavaScript kullanılmayacaktır.

Global değişken oluşturulmayacaktır.

Kod modüler olacaktır.

---

# Güvenlik Kuralları

CSRF koruması

XSS koruması

SQL Injection koruması

Clickjacking koruması

Rate Limiting

Input Validation

Output Escaping

Güçlü parola politikası

Yetkilendirme kontrolü

Dosya yükleme güvenliği

---

# Performans Kuralları

Lazy Loading

Pagination

Image Optimization

Caching

Database Index

Static Compression

Minimum sorgu

Minimum JavaScript

Minimum CSS

---

# SEO Kuralları

Her sayfanın benzersiz;

Title

Meta Description

Canonical URL

OpenGraph

Twitter Card

JSON-LD

Breadcrumb

bulunmalıdır.

URL yapısı SEO dostu olmalıdır.

---

# UI / UX Kuralları

Minimalist

Modern

Kurumsal

Güven veren

Hızlı

Mobil uyumlu

Tutarlı

Erişilebilir

tasarım kullanılacaktır.

Her bileşen profesyonel görünmelidir.

---

# Dosya Organizasyonu

Her klasörün tek amacı vardır.

Kod doğru klasörde bulunmalıdır.

Geçici kod bırakılmaz.

Deneme kodu bırakılmaz.

Kullanılmayan dosya bırakılmaz.

---

# Dokümantasyon

Yeni eklenen her özellik;

README

ROADMAP

ARCHITECTURE

gerekliyse güncellenmelidir.

---

# Test Politikası

Yeni özellik test edilmeden tamamlanmış kabul edilmez.

Model

View

Service

Selector

Validator

testleri yazılmalıdır.

---

# Refactoring

Kod çalışıyor diye bırakılmaz.

Daha okunabilir hale getirilebiliyorsa düzeltilir.

Tekrar eden kod kaldırılır.

Performans artırılabiliyorsa artırılır.

---

# Yasaklar

Business Logic View içerisinde yazmak.

Business Logic Template içerisinde yazmak.

Business Logic JavaScript içerisine yazmak.

Raw SQL kullanmak (zorunlu olmadıkça).

Inline CSS.

Inline JavaScript.

Kopyala-yapıştır kod.

Tekrar eden kod.

Hardcoded değerler.

Magic Number.

Performansı düşüren sorgular.

Test edilmemiş kod.

Dokümantasyonsuz özellik eklemek.

Mimariyi bozan değişiklik yapmak.

---

# Yapay Zekanın Karar Verme Önceliği

Her öneri aşağıdaki sıraya göre değerlendirilmelidir.

1. Güvenlik
2. Veri bütünlüğü
3. Yazılım mimarisi
4. Performans
5. Ölçeklenebilirlik
6. Bakım kolaylığı
7. Kod okunabilirliği
8. Kullanıcı deneyimi
9. SEO
10. Görsel tasarım

---

# Nihai Hedef

Bu proje;

Türkiye'nin en güvenilir,

en hızlı,

en kaliteli,

en profesyonel,

en sürdürülebilir,

en ölçeklenebilir

yöresel yemek platformlarından biri olacak şekilde geliştirilecektir.

Hiçbir geliştirme kısa vadeli düşünülerek yapılmayacaktır.

Her mimari karar gelecekte yüz binlerce kullanıcı ve on binlerce tarifi destekleyecek şekilde alınacaktır.
```
