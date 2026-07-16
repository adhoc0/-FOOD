# CHANGELOG

Bu proje [Semantic Versioning](https://semver.org/) kullanır. Proje alpha aşamasında
olduğu için `0.x` sürümlerinde geriye dönük uyumsuz değişiklikler yapılabilir.

## [Unreleased]

### Changed

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

### Removed

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
