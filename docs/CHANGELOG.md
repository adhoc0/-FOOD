# CHANGELOG

Bu proje [Semantic Versioning](https://semver.org/) kullanır. Proje alpha aşamasında
olduğu için `0.x` sürümlerinde geriye dönük uyumsuz değişiklikler yapılabilir.

## [Unreleased]

### Added

- Giriş brute-force koruması: kullanıcı adı bazlı başarısız deneme sayacı (5 deneme / 15 dk kilit), `ThrottledAuthenticationForm`.

- Production dağıtımı: `docker-compose.prod.yml`, TLS'li Nginx şablonu, Let's Encrypt kurulum betiği, `.env.prod.example`.
- `REDIS_URL` ile Redis cache desteği (`config/cache.py`); log formatına zaman ve logger adı eklendi.

- Test kapsamı %92,85'e çıkarıldı; CI'da `pytest --cov` ve `fail_under = 90` eşiği.

- Özel 404 ve 500 hata sayfaları (`templates/404.html`, `templates/500.html`).
- `/robots.txt` (hesap/etkileşim/arama yolları kapalı, sitemap bağlantılı).

### Removed

- Gölgelenen ölü `provinces/admin.py` (gerçek admin `provinces/admin/` paketinde).

- Hiçbir yerden referans verilmeyen 52 boş CSS/JS/şablon dosyası silindi.

### Changed

- `docs/SEO.md` URL örnekleri gerçek yapıyla (`/tarifler/...`) uyumlu hale getirildi.

- Proje durumu gerçek geliştirme seviyesiyle uyumlu olacak şekilde alpha olarak tanımlandı.
- ROADMAP, tamamlanan ve bekleyen işleri gösterecek biçimde güncellendi.
- Statik sayfa view'ları doğrudan asıl şablonlara bağlandı.
- Büyük çalışma ağacını atomik commitlere ayırmak için sınıflandırma planı eklendi.
- Test ayarları, test PostgreSQL compose dosyası ve temel CI kalite hattı eklendi.
- Uygulama testlerinin toplanmasını engelleyen yanlış accounts test import'u düzeltildi.
- Test ortamında production HTTPS yönlendirmesinin test istemcilerini etkilemesi düzeltildi.
- Mevcut kullanım şartları şablonu için eksik URL ve view bağlantısı tamamlandı.
- Rating puanı servis ve PostgreSQL constraint ile 1–5 aralığında zorunlu kılındı.
- RecipeImage model ve service girişlerine boyut, uzantı ve magic-byte doğrulaması bağlandı.
- Faz 2 veri bütünlüğü regresyon testleri eklendi.
- Hassas POST uçları için cache tabanlı rate limiting middleware'i eklendi.
- CSP ve Permissions-Policy başlıkları merkezi security middleware'ine eklendi.
- Rate limiting ve güvenlik başlıkları için birim testleri eklendi.
- Kaynak ağacında bilinen secret anahtar biçimleri için tarama yapıldı; gerçek secret bulunmadı.
- Etkileşim ve yönetim uçları için anonim erişim permission testleri eklendi.
- pip-audit bulguları doğrultusunda Django 6.0.7 ve Pillow 12.3.0 güvenli sürümlerine yükseltildi.
- Faz 3 başlangıcında inline stiller kaldırılarak CSP ve erişilebilirlik uyumu güçlendirildi.
- Production ortamı için HTTPS, HSTS ve secure cookie ayarlarının DEBUG=False altında doğrulaması yapıldı.

### Fixed

- `sitemap.xml` kullanım şartları sayfasını (`pages:terms`) içermiyordu; eklendi.

- Girişten sonra var olmayan `/accounts/profile/` adresine yönlendirme düzeltildi; giriş profile, çıkış ana sayfaya gider.
- Şifre sıfırlama akışının URL'leri ve e-posta şablonları eklendi.
- Hız sınırı, Nginx arkasında tüm anonim istemcileri tek IP sayıyordu; `NUM_PROXIES` ile güvenilen proxy sayısına göre istemci IP'si çözülür.
- Ana sayfa haritasındaki il tıklaması il detay sayfasına gider; tooltip ve erişilebilir etiketler il adını gösterir.
- İl detay sayfası taslak ve pasif tarifleri de listeliyordu; yalnızca yayındaki tarifler gösterilir.
- Harita rengi doğrulaması satır sonu karakteriyle biten değeri kabul ediyordu.
- Yorum/puan formunda geçersiz veya boş gönderimler sessizce yok sayılıyordu; kullanıcıya mesaj gösterilir.

### Changed (mimari)

- Arama filtreleme ve sıralama mantığı `SearchView` içinden `RecipeSelector.search_published` ve `RecipeQuerySet.sort_by` katmanına taşındı; "popular" sıralaması tek tanıma bağlandı (önce favori, sonra görüntülenme).
- Arama sonuçları ilişkili il ve kategoriyle birlikte yüklenir (N+1 sorgu giderildi); toplam sonuç sayısı paginator'dan alınır.
- Puan istatistiği yalnızca Rating sinyalinde hesaplanır; favori sayacı kodu `RecipeService` içinde tekilleştirildi.
- Test factory'sindeki kullanıcı parolası artık veritabanına kaydedilir.

### Removed

- Hiçbir yerde güncellenmeyen `Recipe.comment_count` alanı kaldırıldı (migration `0004`).
- `ProvinceManager` için ikinci (tekrar eden) tanım kaldırıldı.
- Var olmayan uygulama klasörleri paket ve coverage listelerinden çıkarıldı; `common` eklendi.
- Django dinamik sitemap endpoint'iyle çakışan boş kök `sitemap.xml` kaldırıldı.
- Yalnızca başka bir şablonu genişleten gereksiz statik sayfa ara şablonları kaldırıldı.
- Kullanılmayan toplu `pages.views.views` modülü kaldırıldı.

## [0.3.0] - 2026-07-16

### Added

- Accounts, provinces, recipes, pages ve interactions uygulamalarının temel yapıları.
- Service, selector, validator ve özel queryset katmanlarının başlangıç uygulamaları.
- Region, Province, Recipe, Category, Cuisine, Ingredient, Tag, Favorite, Rating ve Comment modelleri.
- Docker, Gunicorn, Nginx ve PostgreSQL geliştirme yapılandırmaları.
- Temel sitemap, SEO bileşenleri, test fabrikaları ve otomatik testler.

### Known Issues

- PostgreSQL servisi olmadan veritabanı kullanan testler çalışmıyor.
- Uygulama içi bazı test klasörleri mevcut pytest toplama kapsamının dışında.
- Production e-posta, HTTPS, rate limiting, monitoring ve backup doğrulanmış değil.
- Çalışma ağacı henüz mantıksal ve atomik commitlere ayrılmadı.

## Sürümleme Kuralları

- Kullanıcıyı veya geliştiriciyi etkileyen değişiklikler kaydedilir.
- Başlıklar `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed` ve `Security` biçimindedir.
- Sürüm kayıtları tarih içerir ve en yeni kayıt üstte tutulur.
- Yalnızca biçimlendirme ve davranış değiştirmeyen küçük düzenlemeler kaydedilmez.
