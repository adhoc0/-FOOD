# ÇALIŞMA AĞACI DÜZENLEME PLANI

Bu belge, mevcut büyük değişiklik kümesinin hangi mantıksal gruplar halinde gözden
geçirilip commitlenmesi gerektiğini tanımlar. Dosyalar doğrulanmadan toplu commit
oluşturulmamalıdır.

## 1. Proje Yapılandırması

- `pyproject.toml`
- `mypy.ini`
- `manage.py`
- `core/`
- `common/`
- `requirements/`
- `.dockerignore`

Önerilen commit: `build: align project configuration with alpha release`

## 2. Accounts Alanı

- `accounts/models/`
- `accounts/managers/`
- `accounts/selectors/`
- `accounts/services/`
- `accounts/validators/`
- Accounts form, view, URL, admin ve migration dosyaları

Önerilen commit: `refactor: establish layered accounts architecture`

## 3. Provinces Alanı

- Province ve Region model/queryset/manager dosyaları
- Selector, service, validator ve admin dosyaları
- İl veri yükleme komutu ve migration dosyaları

Önerilen commit: `refactor: consolidate province domain layers`

## 4. Recipes Alanı

- Model ve migration değişiklikleri
- Queryset, selector, service ve validator katmanları
- Admin, form, signal, URL ve view dosyaları
- Seed veri dosyaları

Bu grup büyüktür. Model/migration, okuma katmanı, yazma katmanı ve HTTP katmanı
ayrı ayrı doğrulanmalı ve mümkünse ayrı commitlenmelidir.

## 5. Interactions Alanı

- Favorite, Rating ve Comment modelleri
- Service ve validator dosyaları
- View, URL, signal ve admin değişiklikleri

Önerilen commit: `refactor: move interaction rules into services`

## 6. Pages ve SEO

- `pages/`
- Sitemap sınıfları
- Meta, canonical, OpenGraph ve JSON-LD şablonları
- Statik politika sayfaları

Önerilen commit: `feat: establish page and SEO foundations`

## 7. Frontend

- `templates/`
- `static/css/`
- `static/js/`
- `static/images/`

Boş dosyalar ve alternatif component yapıları commit öncesinde tekrar kontrol
edilmelidir. Davranış içeren JavaScript, ona ait template ve CSS ile birlikte
gözden geçirilmelidir.

## 8. Testler

- `tests/factories/`
- `tests/unit/`
- `tests/integration/`
- Uygulama içi test klasörleri

Test toplama yapılandırması Faz 1 konusudur. Faz 0 sırasında test dosyaları kaynak
kod değişikliklerinden ayrı tutulmalıdır.

## 9. Deployment

- `Dockerfile`
- `docker-compose.yml`
- `entrypoint.sh`
- `nginx/`

Önerilen commit: `build: prepare containerized development stack`

## 10. Dokümantasyon

- `README.md`
- `docs/`
- Proje çalışma kuralları

Geçici raporlar, görev listeleri ve dizin ağaçları ayrı değerlendirilmelidir;
ürün dokümantasyonu olarak doğrulanmadıkları sürece release commitine eklenmemelidir.

## Commit Öncesi Kontrol

Her grup için:

1. `git diff -- <grup>` ile kapsamı kontrol et.
2. Silinen dosyaların yerine geçen dosyaların gerçekten izleneceğini doğrula.
3. Ruff ve Django sistem kontrolünü çalıştır.
4. İlgili testleri çalıştır.
5. Migration değişikliklerinde ileri yönlü yükseltme yolunu doğrula.
6. Tek amaçlı ve açıklayıcı commit mesajı kullan.

Ana dal üzerinde doğrudan commit oluşturulmamalıdır. Çalışma, uygun bir refactor
veya stabilization dalında sürdürülmelidir.
