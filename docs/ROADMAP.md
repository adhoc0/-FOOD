# ROADMAP

## Proje Durumu

- Sürüm: `0.3.0` (alpha)
- Aşama: Temel alan modelleri ve kullanıcı etkileşimleri geliştiriliyor.
- Yayın durumu: Production'a hazır değil.
- Aktif uygulamalar: `accounts`, `pages`, `provinces`, `recipes`, `interactions`.
- Temel risk: Büyük ve henüz atomik commitlere ayrılmamış çalışma ağacı.

## Tamamlanan Temel Altyapı

- Django 6 ve Python 3.14 proje yapısı
- PostgreSQL bağlantı yapılandırması
- Custom User modeli
- Region, Province, Recipe, Category, Cuisine, Ingredient ve Tag modelleri
- Favori, puan ve yorum modelleri
- Service, selector, validator ve queryset katmanlarının başlangıç yapısı
- Docker, Gunicorn ve Nginx geliştirme altyapısı
- Ruff yapılandırması ve temel test paketi
- Dinamik sitemap ve temel SEO şablonları

Bu maddeler tamamlanmış ürün özelliği anlamına gelmez. Her modülün test, güvenlik,
erişilebilirlik ve production doğrulaması ayrıca tamamlanmalıdır.

## Mevcut Çalışma — Faz 0

- [x] Projenin mevcut durumunu mimari ve güvenlik açısından denetle
- [x] Gerçek sürümü alpha olarak işaretle
- [x] ROADMAP ve CHANGELOG'u gerçek durumla eşleştir
- [x] Dinamik sitemap ile çakışan boş statik sitemap dosyasını kaldır
- [x] Gereksiz statik sayfa şablon yönlendirme katmanlarını kaldır
- [x] Mevcut büyük değişiklik kümesi için mantıksal commit planı hazırla
- [ ] Planlanan grupları ayrı dallarda doğrulayıp atomik commitlere ayır
- [ ] Eski ve yeni paralel dosyaların kalanlarını dosya bazında sınıflandır
- [ ] Geçici analiz ve ağaç çıktılarının saklama politikasını kararlaştır

## Mevcut Aşama — Faz 1: Test ve Doğrulama Altyapısı

- [x] Ayrı test settings modülü
- [x] Docker tabanlı test PostgreSQL'i
- [x] Bütün uygulama test klasörlerinin pytest tarafından toplanması
- [x] Migration, lint, test ve güvenlik kontrollerinin CI üzerinde çalıştırılması
- [x] PostgreSQL üzerinde tüm mevcut testleri çalıştır
- [ ] Kritik kullanıcı ve veri bütünlüğü akışlarının test kapsamını tamamla

## Planlanan Ürün Sırası

1. Veri bütünlüğü ve güvenlik
2. Mimari sadeleştirme
3. İl, kategori ve tarif liste/detay akışları
4. Arama ve filtreleme
5. Kullanıcı hesabı ve profil akışları
6. Favori, puan, yorum ve moderasyon
7. SEO, erişilebilirlik ve performans doğrulaması
8. Staging ve production deployment

## Yayın Öncesi Zorunlu Koşullar

- Tüm otomatik testler geçmeli
- Migration geçmişi ileri yönlü ve doğrulanmış olmalı
- Yetkilendirme, dosya yükleme ve rate limiting tamamlanmalı
- Production settings, HTTPS, e-posta, loglama ve backup doğrulanmalı
- Lighthouse, erişilebilirlik ve sorgu sayısı ölçümleri yapılmalı
- ROADMAP, CHANGELOG ve mimari karar kayıtları güncel olmalı

## Uzun Vadeli Konular

Redis, Celery, API, çoklu dil, mobil uygulama, öneri sistemi ve premium özellikler;
çekirdek ürün production kalitesine ulaşmadan geliştirme kapsamına alınmayacaktır.
