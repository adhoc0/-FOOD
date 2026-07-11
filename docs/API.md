# API

## Amaç

Bu doküman projedeki API geliştirme standartlarını tanımlar.

Tüm API endpoint'leri bu kurallara uygun geliştirilmelidir.

---

# Genel Kurallar

- REST mimarisi kullanılacaktır.
- Endpoint isimleri tutarlı olmalıdır.
- Türkçe URL kullanılmayacaktır.
- JSON formatı kullanılacaktır.
- UTF-8 kullanılacaktır.
- API versiyonlanacaktır.

Örnek

/api/v1/

---

# HTTP Metotları

GET

- Veri okuma

POST

- Yeni kayıt oluşturma

PUT

- Kaydı tamamen güncelleme

PATCH

- Kısmi güncelleme

DELETE

- Silme işlemi

---

# URL Standartları

Doğru

/api/v1/recipes/

/api/v1/categories/

/api/v1/provinces/

/api/v1/ingredients/

Yanlış

/getRecipes

/createRecipe

/deleteRecipe

---

# Response Formatı

Başarılı cevap

{
    "success": true,
    "data": {}
}

Hatalı cevap

{
    "success": false,
    "message": "",
    "errors": {}
}

---

# HTTP Status Kodları

200 OK

201 Created

204 No Content

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

405 Method Not Allowed

409 Conflict

422 Validation Error

500 Internal Server Error

---

# Pagination

Liste endpoint'lerinde pagination zorunludur.

Standart

page

page_size

Örnek

/api/v1/recipes/?page=1&page_size=20

---

# Filtering

Filtreleme Query Parameter ile yapılmalıdır.

Örnek

?province=ankara

?category=corba

?difficulty=easy

?is_featured=true

---

# Searching

Arama

?q=

Örnek

/api/v1/recipes/?q=mantı

---

# Sorting

Sıralama

?ordering=

Örnek

?ordering=name

?ordering=-created_at

---

# Authentication

Kimlik doğrulama gerektiren endpoint'ler korunmalıdır.

Anonymous kullanıcı yalnızca izin verilen endpoint'lere erişebilir.

---

# Authorization

Yetkilendirme View seviyesinde yapılmalıdır.

Permission sınıfları kullanılmalıdır.

---

# Validation

Tüm kullanıcı verileri doğrulanmalıdır.

Serializer validation kullanılmalıdır.

Model validation kullanılmalıdır.

---

# Rate Limit

API Rate Limit uygulanmalıdır.

Anonim kullanıcı

Düşük limit

Giriş yapan kullanıcı

Daha yüksek limit

---

# Security

CSRF koruması

XSS koruması

SQL Injection koruması

CORS ayarları

HTTPS zorunludur.

---

# Versioning

Yeni sürümler

/api/v2/

şeklinde oluşturulmalıdır.

Eski sürümler hemen kaldırılmaz.

---

# Logging

API hataları loglanmalıdır.

500 hataları raporlanmalıdır.

---

# Performance

select_related()

prefetch_related()

Pagination

Cache

zorunlu değerlendirilmelidir.

---

# Documentation

Her endpoint aşağıdaki bilgileri içermelidir.

- Amaç
- URL
- HTTP Metodu
- Parametreler
- Request Body
- Response
- Hata Kodları
- Authentication Durumu

---

# Yasaklar

Türkçe endpoint

CamelCase URL

Raw SQL

N+1 Query

Hardcoded ID

Validation olmayan endpoint

Authentication olmayan kritik endpoint

Pagination olmayan liste endpoint'leri

GET ile veri değiştirme

DELETE isteğinde GET kullanma

POST yerine GET kullanma