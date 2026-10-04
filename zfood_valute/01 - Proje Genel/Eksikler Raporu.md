---
title: Eksikler Raporu (2026-09-29)
tags:
  - food-project
  - audit
  - roadmap
date: 2026-09-29
---
# 🔍 Eksikler Raporu

Kod, doküman, Docker/CI ve statik dosyaların okunarak yapılan incelemesi. **Testler çalıştırılmadı** (ortamda Python 3.14, PostgreSQL ve Docker yoktu); bulgular kod okumasına dayanır. İlgili notlar: [[Yol Haritası (Roadmap)]], [[Değişiklik Günlüğü]], [[Clean Architecture]], [[Güvenlik Rehberi]], [[SEO ve Performans]], [[Production Kontrol]], [[Test Stratejisi]].

**Durum özeti:** 5 aktif uygulama (accounts, pages, provinces, recipes, interactions), ~8 bin satır Python, ~160 test, sürüm 0.3.0 alpha. Katmanlı mimari büyük ölçüde uygulanmış.

---

## 1. Çalışmayan veya bozuk olanlar

> 2026-10-01: İşaretli maddeler düzeltildi; `pytest` çalıştırıldı, **179 test geçti** (Windows, `.venv`). Kalan: `media/recipes/` temizlendi; boş/`pass` test dosyaları (recipes, provinces) hâlâ doldurulmayı bekliyor.

- [x] **Girişten sonra 404:** `LOGIN_REDIRECT_URL` / `LOGOUT_REDIRECT_URL` tanımsız (settings'te yarım yorum satırı). Django varsayılanı `/accounts/profile/` mevcut değil.
- [x] **Şifre sıfırlama çalışmıyor:** 4 şablon var, `accounts/urls.py`'de URL yok. Rate limit listesi de var olmayan `/hesap/password-reset/` yolunu koruyor.
- [x] **Rate limit canlıda herkesi tek kullanıcı sayar:** IP için `REMOTE_ADDR` kullanılıyor; Nginx arkasında hep proxy adresi olur (`X-Forwarded-For` okunmuyor). Sayaçlar `LocMemCache`'te, worker başına ayrı.
- [x] **Harita:** İl tıklaması il detayına değil listeye gidiyor; tooltip'te il adı yok ("İl 06"), plaka koduna göre çalışıyor.
- [x] **İkonlar görünmüyor:** 15 yerde Font Awesome sınıfı var, kütüphane yüklenmiyor (CSP `font-src 'self'`). Login'deki `glassmorphism` sınıfının CSS'i yok.
- [x] **Testler boş (kısmen):** `recipes/tests/unit/*` 6 dosya 0 bayt; `provinces/tests/*` 9 dosya yalnızca `pass`; `interactions/tests.py` şablon. En büyük modül (recipes, ~4.7 bin satır) kendi klasöründe test edilmiyor.
- [x] **Testler gerçek `media/` klasörünü kirletiyor:** `media/recipes/` içinde 105 `example_*.jpg`. `MEDIA_ROOT` test için izole değil.

## 2. İçerik ve ürün eksikleri

- [ ] **Veri yok denecek kadar az:** 2 kategori, 3 malzeme, 2 etiket; `recipes/data/recipes/` boş; `fixtures/provinces.json` 0 bayt (81 il yalnızca `load_provinces` komutunda). Cuisine/tag/ingredient seed komutu yok.
- [ ] **Kullanıcı tarif ekleyemiyor:** `recipe_form.py` var, oluşturma view'ı/URL'i yok. Bilinçli karar mı belgelenmemiş.
- [ ] **Bitmemiş sayfalar:** 13 boş şablon (`contact_form`, `newsletter_form`, tarif detay partial'larının 9'u ...). Bülten kapalı; iletişim sayfasında form yok, e-posta sahte domain (`.example`).
- [ ] **Frontend:** 31 JS dosyasının 25'i boş (`api.js`, `favorite.js`, `rating.js`, `comment.js`, `search.js` ...). Boş CSS'ler: `dark.css`, `search.css`, `profile.css` vb. Favori/puan/yorum tam sayfa POST ile çalışıyor.
- [ ] **Kayıt akışı:** e-posta doğrulama yok, otomatik giriş yok, başarı adresi `"/"` sabit; profil düzenleme ve parola değiştirme yok; e-posta backend'i yalnızca konsol.
- [ ] **Marka adı tutarsız:** "Lezzet Haritası" / "Yöresel Lezzetleri" / "Türkiye Yöresel Yemekleri".
- [ ] **Arama:** tarif listesi yalnızca il+kategori süzüyor; malzeme ve etiket sayfaları yok. `SearchService` içeriği ayrıca doğrulanmalı.

## 3. Mimari kural ihlalleri

- [x] `SearchView` içinde filtreleme ve sıralama haritası (selector'a taşınmalı).
- [x] `add_comment` view'ında 1–5 kuralı tekrarlanıyor; yorum ve puan tek endpoint'te karışık; geçersiz puan sessizce yok sayılıyor; içerik ve puan boşsa mesaj yok.
- [x] Puan istatistiği iki kez hesaplanıyor (`RatingService.rate` + `post_save` signal); signal başka uygulamanın private metodunu çağırıyor.
- [x] Favori sayacı kodu `FavoriteService` ve `RecipeService`'te tekrar ediyor.
- [ ] Uygulama sınırı ters: `interactions` modelleri `recipes`'i import ediyor, `RatingService`/`FavoriteService` ise `recipes` içinde.
- [x] `Recipe.comment_count` hiçbir yerde güncellenmiyor (hep 0).
- [ ] `RecipeDetailView` her GET'te veritabanına yazıyor ve tekrar okuyor; bot ve tekrar ziyaret filtresi yok.
- [ ] `unique_together` yerine `UniqueConstraint` tercih edilmeli.
- [x] `analytics`, `api`, `notifications`, `search`, `sitemaps`, `storage`, `management` boş klasör ama `pyproject.toml` paket/coverage kaynağı olarak listeliyor.

## 4. SEO ve erişilebilirlik

- [x] `robots.txt` eklendi (sitemap bağlantılı). [ ] `humans.txt` hâlâ servis edilmiyor (kökte dosya duruyor).
- [x] 404/500 şablonları eklendi (`templates/404.html`, `500.html`); testli.
- [x] (`docs/SEO.md` düzeltildi; ayrı malzeme yolu uygulamada yok) [[SEO ve Performans]] dokümanındaki URL'ler (`/tarif/...`, `/kategori/...`, `/malzeme/...`) uygulamadakilerle (`/tarifler/...`, `/tarifler/kategori/...`) uyuşmuyor; malzeme yolu yok.
- [x] Harita SVG yolları `role="button"` ama etiket yalnızca "İl 06"; il adı yok.
- [ ] Lighthouse, WCAG ve sorgu sayısı ölçümleri yapılmamış (yol haritası bunları yayın öncesi zorunlu sayıyor).

## 5. Deployment ve altyapı

- [x] (Dosyalar hazır, sunucuda denenmedi: `docker-compose.prod.yml`, TLS Nginx, certbot betiği) Production yapılandırması yok: `docker-compose.yml` yalnızca geliştirme (`DEBUG=True`); prod compose, HTTPS/TLS, Let's Encrypt, gerçek `server_name` yok; Nginx yalnızca :80 ve CSP eklemiyor.
- [ ] Bağımlılıklar iki yerde: `pyproject.toml` (`Django>=6.0.7`) vs `requirements/*.txt` (`>=6.0`); Docker imajı requirements'tan kuruluyor, `gunicorn` yalnızca `prod.txt`'te. Güvenlik yükseltmeleri imaja yansımayabilir.
- [x] (Redis cache `REDIS_URL` ile eklendi; Celery hâlâ yok) Redis/Celery yok (`config/celery.py` yalnızca açıklama); cache `LocMemCache`.
- [ ] Loglama yalnızca konsol; güvenlik/audit logu, rotasyon, hata izleme (Sentry vb.) yok.
- [ ] Backup, izleme ve sağlık kontrolü uygulaması yok (yalnızca dokümanda).
- [ ] CI: `pip-audit` (bilgilendirme amaçlı) ve Docker build işi eklendi; coverage eşiği (%90), mypy ve deploy adımı hâlâ yok.
- [x] Brute-force: kullanıcı adı bazlı kilit eklendi (cache tabanlı, paket yok). [ ] 2FA hâlâ yok.

## 6. Süreç ve dokümantasyon

- [ ] **Git durumu yanıltıcı:** `git status` 99 değişiklik gösteriyor, satır sonları yok sayılınca gerçek fark 14 dosya. `.gitattributes` yok (CRLF/LF). [[Yol Haritası (Roadmap)]]'taki "büyük çalışma ağacı" riski abartılı görünüyor.
- [ ] İzlenmeyen: `food_obsidian_vault.zip`, `zfood_valute/`. `.envs/` altındaki 3 boş env dosyası Git'te.
- [ ] `docs/ARCHITECTURE.md` bölüm 1 ve 4 şablon cümlelerinde kalmış; `docs/DECISIONS.md` yalnızca ADR-001 içeriyor (CustomUser, Django 6/Python 3.14, vanilla JS gibi kararlar kayıtsız) → [[Mimari Kararlar (ADR)]].
- [ ] `PROJE_ANALIZ_RAPORU.md` (11 Temmuz) eski: rate limiting ve CSP eklenmiş ama rapor eksik diyor.
- [ ] `docs/API.md` DRF ve `/api/v1/` anlatıyor; DRF kurulu değil, `api/` uygulaması yok.
- [ ] `.agents/skills` ve `.agents/prompts` ile proje kuralları senkron mu belirsiz.

---

## Önerilen sıra

1. Login yönlendirmesi, şifre sıfırlama URL'leri, rate limit IP sorunu.
2. `.gitattributes`, ardından boş testleri doldurmak ve test `MEDIA_ROOT`'unu izole etmek.
3. Mimari düzeltmeler: `SearchView` → selector, signal/servis çift hesaplama, `comment_count`.
4. Veri: 81 il fixture'ı, gerçek kategori, malzeme ve ilk tarifler.
5. Frontend: boş JS/CSS'i doldur veya sil, harita → il detayı, 404/500, `robots.txt`.
6. Production hattı: prod compose, HTTPS, tek bağımlılık kaynağı, Redis, loglama, CI'a coverage ve pip-audit.

---

## Güncelleme (2026-10-01)

- provinces için birim ve entegrasyon testleri yazıldı; recipes için `SearchService`, `CategoryService`, `CategoryValidator` ve `CategoryQuerySet` testleri eklendi. **Henüz çalıştırılmadı.**
- Testler sırasında bulunup düzeltilenler: il detay sayfası taslak/pasif tarifleri de listeliyordu (artık yalnızca yayındakiler); `validate_map_color` satır sonlu değeri kabul ediyordu (`fullmatch` ile düzeltildi).
- Hâlâ açık: `recipes/tests/unit/test_models.py`, `test_views.py`, `test_forms.py` boş; cuisine, ingredient ve tag servis/validator testleri yok; `SearchService` sonuçlarında `select_related` yok (arama sayfasında N+1 olasılığı); `ProvinceManager` iki yerde tanımlı.

## Güncelleme — mimari düzeltmeler (2026-10-01)

Kodda yapıldı, **henüz çalıştırılmadı** (`python -m pytest -q` ve `python manage.py makemigrations --check` gerekir): `SearchView` mantığı selector'a taşındı, `add_comment` hataları kullanıcıya gösteriliyor, puan istatistiği tek noktadan (sinyal) hesaplanıyor, favori sayacı tekilleştirildi, `comment_count` kaldırıldı (migration `0004`), `ProvinceManager` tekrarı ve var olmayan paket listeleri temizlendi.

Bilinçli olarak yapılmayanlar:
- [ ] Detay sayfasında görüntülenme sayacı her GET'te yazıyor; oturum başına tekilleştirme ayrı bir tasarım kararı.
- [ ] `unique_together` → `UniqueConstraint` geçişi (migration gerektirir, ayrı commit olmalı).
- [ ] `FavoriteService` / `RatingService` `recipes` içinde, modelleri `interactions` içinde; taşınması ADR ile karara bağlanmalı.
- [ ] Favori/puan/yorum view'ları hâlâ tam sayfa POST ve yönlendirme ile çalışıyor.

## Güncelleme — SEO ve temizlik (2026-10-04)

Yapıldı: özel 404/500, `robots.txt`, 53 boş/kullanılmayan statik ve şablon dosyası silindi, boş test iskeletleri silindi, tarif model/view/form testleri eklendi, CI'a `pip-audit` ve Docker build işi eklendi. Kullanıcı tarafında `makemigrations --check` temiz ve hata sayfası testleri geçti; tam `pytest` çıktısı bu notta doğrulanmadı.

## Güncelleme — test kapsamı (2026-10-04)

Doğrulandı (kullanıcı çıktısı): `pytest` 401 geçti, toplam kapsama %92,85. Eşik `fail_under = 90` yapıldı; wsgi/asgi/gunicorn/management komutları kapsam dışı. Silinen: boş `accounts` test iskeletleri, ölü `recipes/models.py`.
Kalan kapsama boşlukları: `provinces/admin.py`, `pages/sitemaps.py`, `recipe_form.py` clean dalları, `base_validator.validate_decimal`, `recipe_image_service` silme/sıralama dalları.

## Güncelleme — production (2026-10-04)

`docker-compose.prod.yml`, `nginx/nginx.prod.conf.template`, `scripts/init-letsencrypt.sh`, `.env.prod.example`, Redis cache ayarı ve `docs/DEPLOYMENT.md` bölümü eklendi. **Gerçek sunucuda veya `docker compose config` ile doğrulanmadı.** Açık: yedekleme, hata izleme (Sentry), brute-force koruması, 2FA, deploy adımı.

## Güncelleme — kapsama ve güvenlik (2026-10-05)

Doğrulandı (kullanıcı çıktısı): 444 test geçti, kapsama %95,62; eşik `fail_under = 93`. Giriş brute-force kilidi, sitemap `terms` düzeltmesi, ölü `provinces/admin.py` ve `recipes/models.py` temizliği yapıldı. CI'a mypy bilgilendirme adımı eklendi; **mypy yerelde çalıştırılmadı** (kurulu değil), hata sayısı bilinmiyor. Açık: mypy temizliği, 2FA, yedekleme, hata izleme (Sentry), deploy adımı, görüntülenme sayacı tekilleştirme.
