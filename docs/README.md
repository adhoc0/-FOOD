# Türkiye Yöresel Yemekleri

Türkiye'nin tüm yöresel lezzetlerini tek bir platformda buluşturan, güvenilir, hızlı, modern ve ölçeklenebilir bir gastronomi platformu.

Bu proje yalnızca bir yemek tarifi sitesi değildir.

Amaç, Türkiye'nin gastronomi kültürünü dijital ortama profesyonel bir şekilde taşımak, her ilin yöresel yemeklerini doğru bilgilerle sunmak ve uzun yıllar geliştirilebilecek sürdürülebilir bir yazılım altyapısı oluşturmaktır.

---

# Vizyon

Türkiye'nin en kapsamlı ve en güvenilir yöresel yemek platformu olmak.

Kullanıcılara yalnızca tarif sunmak değil;

- Türkiye'nin gastronomi kültürünü tanıtmak
- Yöresel mutfakları dijitalleştirmek
- Aranılan her yemeği kolayca bulunabilir hale getirmek
- SEO açısından sektörün en güçlü altyapısını oluşturmak
- Hızlı, güvenli ve modern bir kullanıcı deneyimi sunmak

---

# Temel Özellikler

- Türkiye SVG Haritası
- İl Bazlı Tarif Sistemi
- Bölgelere Göre Filtreleme
- Kategori Sistemi
- Malzeme Bazlı Arama
- Gelişmiş Arama Motoru
- Favori Sistemi
- Puanlama Sistemi
- Yorum Sistemi
- Kullanıcı Profilleri
- SEO Altyapısı
- Responsive Tasarım
- Admin Yönetim Paneli

---

# Teknoloji Yığını

## Backend

- Python
- Django
- PostgreSQL

## Frontend

- HTML5
- CSS3
- Vanilla JavaScript

## Sunucu

- Docker
- Docker Compose
- Gunicorn
- Nginx

## Gelecekte

- Redis
- Celery
- Elasticsearch

---

# Proje Mimarisi

Proje Clean Architecture yaklaşımı temel alınarak geliştirilmektedir.

Katmanlar

- Models
- Services
- Selectors
- Validators
- Views
- Templates
- Static Components

Her katmanın tek sorumluluğu bulunmaktadır.

Business Logic yalnızca Service katmanında yer alır.

---

# Klasör Yapısı

```
accounts/
core/
docs/
interactions/
provinces/
recipes/
static/
templates/
fixtures/
requirements/
```

Her uygulama kendi sorumluluğundan sorumludur.

Kod tekrarına izin verilmez.

---

# Kullanılan Standartlar

- Clean Architecture
- SOLID
- DRY
- KISS
- YAGNI
- PEP8
- Semantic HTML
- Responsive Design
- Component Based Development

---

# Kurulum

## Repository

```bash
git clone <repository-url>

cd FOOD
```

---

## Sanal Ortam

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Paketler

```bash
pip install -r requirements/dev.txt
```

---

## Environment

```
.env
```

dosyasını oluştur.

```
SECRET_KEY=

DEBUG=True

DATABASE_URL=

ALLOWED_HOSTS=
```

---

## Migration

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Superuser

```bash
python manage.py createsuperuser
```

---

## Development Server

```bash
python manage.py runserver
```

---

# Docker

Container oluştur

```bash
docker compose build
```

Başlat

```bash
docker compose up
```

Durdur

```bash
docker compose down
```

---

# Test

Tüm testler

```bash
python manage.py test
```

Belirli uygulama

```bash
python manage.py test recipes
```

---

# Kod Kalitesi

Lint

```bash
ruff check .
```

Format

```bash
ruff format .
```

Type Check

```bash
mypy .
```

---

# Veritabanı

PostgreSQL kullanılmaktadır.

Migration dosyaları manuel değiştirilmez.

ORM dışında sorgu yazılmaz.

---

# Güvenlik

Projede aşağıdaki güvenlik önlemleri uygulanmaktadır.

- CSRF Protection
- XSS Protection
- SQL Injection Protection
- Secure Cookies
- Authentication
- Authorization
- Input Validation
- Output Escaping

---

# Performans

- Pagination
- Image Optimization
- Query Optimization
- select_related
- prefetch_related
- Cache (gelecekte)
- Redis (gelecekte)

---

# SEO

- SEO Friendly URL
- Sitemap
- Robots
- Canonical URL
- OpenGraph
- Twitter Cards
- JSON-LD
- Breadcrumb

---

# Dokümantasyon

Tüm proje dokümantasyonu

```
docs/
```

klasöründe bulunmaktadır.

- AI_CONTEXT.md
- ARCHITECTURE.md
- CHANGELOG.md
- CODING_STANDARDS.md
- DATABASE.md
- DEPLOYMENT.md
- ROADMAP.md
- SECURITY.md
- SEO.md

---

# Geliştirme Kuralları

Her geliştirme öncesinde

- ROADMAP.md
- ARCHITECTURE.md

kontrol edilmelidir.

Yeni özellik eklenirken

- Mimari korunmalıdır.
- Kod standartlarına uyulmalıdır.
- Test yazılmalıdır.
- Dokümantasyon güncellenmelidir.

---

# Sürüm Politikası

Semantic Versioning kullanılmaktadır.

```
MAJOR.MINOR.PATCH
```

---

# Lisans

Bu proje özel geliştirme kapsamında hazırlanmıştır.

İzinsiz kopyalanamaz, dağıtılamaz veya ticari amaçla kullanılamaz.

---

# Katkı

Bu proje bireysel olarak geliştirilmektedir.

Kod kalitesini korumak amacıyla tüm değişiklikler belirlenen mimari ve kodlama standartlarına uygun olmalıdır.

---

# Yol Haritası

Detaylı geliştirme planı

```
docs/ROADMAP.md
```

---

# Mimari

Teknik mimari

```
docs/ARCHITECTURE.md
```

---

# Yapay Zekâ

Projede kullanılan yapay zekâ kuralları

```
docs/AI_CONTEXT.md
```

---

# Nihai Hedef

Türkiye'nin en kaliteli,

en güvenilir,

en hızlı,

en profesyonel,

en sürdürülebilir,

en ölçeklenebilir

yöresel yemek platformlarından birini oluşturmak.