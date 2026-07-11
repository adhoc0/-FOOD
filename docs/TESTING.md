# TESTING

## Amaç

Bu doküman projede uygulanacak test standartlarını tanımlar.

Tüm yeni özellikler uygun testlerle birlikte geliştirilmelidir.

Kod yalnızca çalışıyor olduğu için tamamlanmış kabul edilmez.

---

# Temel Kurallar

- Test yazılmadan kritik özellik tamamlanmış sayılmaz.
- Bug düzeltmelerinde mümkünse önce test yazılır.
- Testler bağımsız çalışmalıdır.
- Testler tekrar çalıştırıldığında aynı sonucu vermelidir.
- Testler production verisini kullanmamalıdır.
- Testler mümkün olduğunca hızlı olmalıdır.

---

# Test Türleri

## Unit Test

Kapsam

- Model
- Service
- Selector
- Validator
- Utility Fonksiyonları

Amaç

Tek bir fonksiyonun veya sınıfın doğru çalıştığını doğrulamak.

---

## Integration Test

Kapsam

- ORM
- PostgreSQL
- Django View
- Authentication
- Permission
- Cache

Amaç

Birden fazla bileşenin birlikte doğru çalışmasını doğrulamak.

---

## API Test

Kontrol Edilecekler

- Status Code
- Response Formatı
- Validation
- Authentication
- Authorization
- Pagination
- Filtering
- Ordering
- Search

---

## UI Test

Kontrol Edilecekler

- Responsive Tasarım
- SVG Haritası
- Formlar
- Navigasyon
- Butonlar
- Accessibility

---

## End-to-End Test

Kontrol Edilecekler

- Kullanıcı Kaydı
- Giriş
- Tarif Görüntüleme
- Tarif Arama
- Favorilere Ekleme
- Yorum Yapma
- Puan Verme

---

# Test Kapsamı

Her Model

- Oluşturma
- Güncelleme
- Silme
- Validation
- Constraint
- Relationship

---

Her Service

- Başarılı Senaryo
- Hatalı Senaryo
- Exception Durumu

---

Her Selector

- Filtreleme
- Sıralama
- Performans
- N+1 Query Kontrolü

---

Her API

- GET
- POST
- PUT
- PATCH
- DELETE

---

# Fixture Kullanımı

Fixture yalnızca

- Region
- Province
- Kategori

gibi değişmeyen veriler için kullanılmalıdır.

Test verileri mümkün olduğunca Factory kullanılmalıdır.

---

# Factory Kullanımı

FactoryBoy tercih edilmelidir.

Her model için Factory oluşturulmalıdır.

Örnek

RecipeFactory

CategoryFactory

ProvinceFactory

UserFactory

IngredientFactory

---

# Mock Kullanımı

Aşağıdaki durumlarda Mock kullanılmalıdır.

- SMTP
- Redis
- Harici API
- Dosya Sistemi
- Cloud Storage

---

# Performans Testi

Kontrol Edilecekler

- Query Sayısı
- Response Süresi
- Memory Kullanımı

N+1 Query oluşmasına izin verilmez.

---

# Güvenlik Testleri

Kontrol Edilecekler

- SQL Injection
- XSS
- CSRF
- Permission
- Authentication
- Rate Limit

---

# Regression Test

Her bug düzeltmesinden sonra regression testi eklenmelidir.

Aynı hata ikinci kez oluşmamalıdır.

---

# Test Komutları

Tüm Testler

python manage.py test

Tek Uygulama

python manage.py test recipes

Tek Dosya

python manage.py test recipes.tests.test_recipe

Tek Test

python manage.py test recipes.tests.test_recipe.RecipeTests.test_create_recipe

Coverage

coverage run manage.py test

coverage report

coverage html

---

# Coverage

Minimum

90%

Hedef

95%

Kritik Modüller

100%

- Authentication
- Permissions
- Payments (ileride eklenirse)
- Security
- Validators

---

# Continuous Integration

Her Pull Request'te

- Testler çalıştırılmalıdır.
- Lint çalıştırılmalıdır.
- Type Check çalıştırılmalıdır.
- Coverage kontrol edilmelidir.

Başarısız test varsa merge yapılmaz.

---

# Test Yazım Kuralları

Her test

Arrange

Act

Assert

düzeninde yazılmalıdır.

Test isimleri açıklayıcı olmalıdır.

Örnek

test_user_can_add_recipe

test_guest_cannot_comment

test_recipe_slug_is_unique

---

# Yasaklar

- Testsiz özellik geliştirmek
- Sleep kullanmak
- Gerçek Production API kullanmak
- Gerçek Production veritabanı kullanmak
- Rastgele çalışan testler
- Bağımlı testler
- Hardcoded ID kullanmak
- print() ile test doğrulamak

---

# Tamamlanmış Sayılma Kriteri

Bir özellik aşağıdaki şartları sağlamadan tamamlanmış kabul edilmez.

- Kod tamamlandı.
- Kod incelendi.
- Test yazıldı.
- Test geçti.
- Lint geçti.
- Type Check geçti.
- Dokümantasyon güncellendi.
- Gerekirse CHANGELOG güncellendi.