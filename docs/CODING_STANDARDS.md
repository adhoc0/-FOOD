````md
# CODING STANDARDS

## Amaç

Bu doküman projede uygulanacak kodlama standartlarını tanımlar.

Amaç;

- Okunabilir kod yazmak
- Sürdürülebilir mimari oluşturmak
- Bakımı kolaylaştırmak
- Performansı artırmak
- Kod tekrarını önlemek
- Profesyonel geliştirme standartlarını korumaktır.

---

# Genel Kurallar

Kod önce insanlar için yazılır.

Derleyici veya yorumlayıcı ikinci plandadır.

Kod mümkün olduğunca açık olmalıdır.

Karmaşık çözümler yerine anlaşılır çözümler tercih edilir.

Kod her zaman geliştirilebilir şekilde yazılır.

---

# Yazılım Prensipleri

Her geliştirme aşağıdaki prensiplere uygun olmalıdır.

- Clean Architecture
- SOLID
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple)
- YAGNI (You Aren't Gonna Need It)
- Separation of Concerns
- Single Responsibility Principle

---

# İsimlendirme Kuralları

## Değişkenler

Anlamlı isimler kullanılmalıdır.

Yanlış

```
a
x
tmp
abc
```

Doğru

```
recipe
province
category
ingredient
user_profile
average_rating
```

---

## Fonksiyonlar

Fonksiyon isimleri yaptığı işi açıkça anlatmalıdır.

Doğru

```
create_recipe()

update_recipe()

delete_recipe()

calculate_average_rating()

get_popular_recipes()
```

---

## Sınıflar

PascalCase kullanılacaktır.

```
Recipe

Province

Category

RecipeService

ProvinceSelector
```

---

## Dosyalar

snake_case kullanılacaktır.

```
recipe_service.py

province_selector.py

image_validator.py
```

---

## Sabitler

UPPER_CASE kullanılacaktır.

```
MAX_IMAGE_SIZE

DEFAULT_PAGE_SIZE

MAX_COMMENT_LENGTH
```

---

# Python Kuralları

PEP8 standardına uyulacaktır.

Satır uzunluğu

120 karakteri geçmemelidir.

Her dosyada import sırası

1. Python
2. Django
3. Third Party
4. Local

şeklinde olacaktır.

Wildcard import kullanılmaz.

```
from x import *
```

yasaktır.

---

# Django Kuralları

Business Logic

View içerisinde yazılmaz.

Business Logic

Model içerisinde yazılmaz.

Business Logic

Template içerisinde yazılmaz.

Business Logic

JavaScript içerisinde yazılmaz.

Business Logic

Service katmanında bulunur.

---

# Models

Her model tek sorumluluğa sahip olacaktır.

Model yalnızca veri tanımlar.

Model içerisinde karmaşık sorgular bulunmaz.

Model içerisinde API çağrısı yapılmaz.

---

# Views

View yalnızca;

Request alır.

Service çağırır.

Response döndürür.

Başka iş yapmaz.

---

# Services

İş kuralları burada bulunur.

Birden fazla modeli ilgilendiren işlemler burada yapılır.

Transaction yönetimi burada yapılır.

---

# Selectors

Karmaşık sorgular burada bulunur.

select_related kullanılmalıdır.

prefetch_related kullanılmalıdır.

N+1 sorgularına izin verilmez.

---

# Validators

Tüm doğrulamalar burada yapılmalıdır.

View doğrulama yapmaz.

---

# Signals

Signal yalnızca otomatik işlemler için kullanılmalıdır.

Signal içerisinde Business Logic bulunmaz.

---

# HTML Kuralları

Semantic HTML kullanılmalıdır.

Tekrar eden HTML component yapılmalıdır.

Accessibility desteklenmelidir.

Form elemanları label içermelidir.

---

# CSS Kuralları

Component tabanlı geliştirme yapılacaktır.

Sayfa bazlı CSS kullanılacaktır.

Global CSS minimum tutulacaktır.

!important kullanılmaz.

Inline CSS kullanılmaz.

Magic Number kullanılmaz.

Responsive tasarım zorunludur.

---

# JavaScript Kuralları

Vanilla JavaScript kullanılacaktır.

Global değişken oluşturulmaz.

Inline JavaScript kullanılmaz.

Kod modüler olacaktır.

Her dosya tek sorumluluğa sahip olacaktır.

---

# SQL Kuralları

Raw SQL kullanılmaz.

ORM tercih edilir.

Index kullanılmalıdır.

Unique Constraint kullanılmalıdır.

Check Constraint kullanılmalıdır.

Transaction kullanılmalıdır.

---

# Güvenlik Kuralları

Tüm kullanıcı girdileri doğrulanmalıdır.

CSRF koruması zorunludur.

SQL Injection koruması zorunludur.

XSS koruması zorunludur.

Dosya yükleme doğrulanmalıdır.

Yetkilendirme kontrol edilmelidir.

Asla gizli bilgi kod içerisine yazılmaz.

---

# Performans Kuralları

N+1 sorgularına izin verilmez.

Pagination kullanılmalıdır.

Lazy Loading kullanılmalıdır.

Görseller optimize edilmelidir.

Cache uygun yerlerde kullanılmalıdır.

Gereksiz sorgu yapılmaz.

---

# Yorum Satırları

Kodun ne yaptığı yazılmaz.

Kodun neden yazıldığı açıklanır.

Gereksiz yorum satırları kullanılmaz.

Eski yorumlar bırakılmaz.

---

# Hata Yönetimi

Sessiz hata yakalanmaz.

```
except:
    pass
```

yasaktır.

Belirli exception yakalanmalıdır.

Loglama yapılmalıdır.

---

# Logging

Error

Warning

Info

Debug

seviyeleri doğru kullanılmalıdır.

Kullanıcı verileri loglanmamalıdır.

Şifreler loglanmaz.

Token'lar loglanmaz.

---

# Test Kuralları

Her yeni özellik test edilmelidir.

Model testleri

View testleri

Service testleri

Selector testleri

Validator testleri

yazılmalıdır.

---

# Git Kuralları

Her commit tek amaç taşımalıdır.

Anlamsız commit mesajları kullanılmaz.

Yanlış

```
update

fix

asd

test
```

Doğru

```
Add province search service

Fix recipe image validation

Optimize recipe queryset

Implement favorite system
```

---

# Kod İnceleme

Kod merge edilmeden önce;

Okunabilirlik

Performans

Güvenlik

Test

Mimari

kontrol edilir.

---

# Yasaklar

Business Logic View içerisinde yazmak.

Business Logic Template içerisinde yazmak.

Business Logic JavaScript içerisinde yazmak.

Wildcard import kullanmak.

Tek harfli değişken isimleri.

Hardcoded değerler.

Magic Number.

Raw SQL (zorunlu olmadıkça).

Inline CSS.

Inline JavaScript.

Kopyala-yapıştır kod.

Tekrar eden kod.

Kullanılmayan kod.

Kullanılmayan import.

Test edilmemiş kod.

Dokümantasyonsuz yeni özellik.

Mimariyi bozan değişiklik.

---

# Kod Yazmadan Önce

Her geliştirmede şu sorular sorulmalıdır.

Bu kod okunabilir mi?

Bu kod tekrar içeriyor mu?

Bu kod test edilebilir mi?

Bu kod performanslı mı?

Bu kod güvenli mi?

Bu kod ölçeklenebilir mi?

Bu kod mimariye uygun mu?

Bu kod daha basit yazılabilir mi?

Bu kod gelecekte bakım yapılabilecek şekilde mi?

Bu kod projenin genel standartlarına uygun mu?
````
