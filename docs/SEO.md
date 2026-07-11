# SEO

## Amaç

Bu doküman projenin Arama Motoru Optimizasyonu (SEO) standartlarını tanımlar.

Amaç;

- Organik trafiği artırmak
- Google'da üst sıralarda yer almak
- Kullanıcı deneyimini geliştirmek
- Yapısal veri standartlarını uygulamak
- Uzun vadeli SEO başarısı sağlamaktır.

SEO, proje tamamlandıktan sonra eklenecek bir özellik değildir.

Her sayfa geliştirilirken SEO kuralları birlikte uygulanacaktır.

---

# SEO Prensipleri

Her sayfa;

- Benzersiz
- Anlamlı
- Hızlı
- Mobil uyumlu
- Yapısal veri içeren
- Kullanıcı odaklı

olmalıdır.

---

# URL Yapısı

URL'ler kısa, okunabilir ve SEO dostu olmalıdır.

Doğru

```
/il/gaziantep/

/il/konya/

/kategori/corbalar/

/tarif/ali-nazik/

/malzeme/patlican/
```

Yanlış

```
/?id=35

/recipe?id=10

/page.php?id=7

/view/2358
```

---

# Slug Kuralları

Slug

- Benzersiz olmalıdır.
- Küçük harf kullanılmalıdır.
- Türkçe karakter dönüştürülmelidir.
- Sonradan değiştirilmemelidir.

Örnek

```
ali-nazik

adana-kebabi

manti

kayseri-yagli-yaprak-sarmasi
```

---

# Sayfa Başlığı (Title)

Her sayfanın benzersiz title etiketi olmalıdır.

Önerilen uzunluk

50-60 karakter

Örnek

```
Ali Nazik Tarifi | Gaziantep Yöresel Yemekleri

Gaziantep Yemekleri | Türkiye Yöresel Yemekleri
```

---

# Meta Description

Her sayfanın benzersiz açıklaması olmalıdır.

Önerilen uzunluk

140-160 karakter

Anahtar kelime doğal şekilde kullanılmalıdır.

---

# Meta Keywords

Kullanılmayacaktır.

Modern arama motorları bu etiketi dikkate almamaktadır.

---

# Canonical URL

Her sayfada canonical etiketi bulunmalıdır.

Kopya içerik engellenmelidir.

---

# Robots

robots.txt kullanılacaktır.

Örnek

```
User-agent: *

Allow: /

Sitemap: https://example.com/sitemap.xml
```

---

# Sitemap

Dinamik sitemap kullanılacaktır.

Ayrı sitemap dosyaları oluşturulacaktır.

```
sitemap.xml

recipes.xml

provinces.xml

categories.xml
```

---

# Open Graph

Her sayfa aşağıdaki alanları içermelidir.

```
og:title

og:description

og:image

og:url

og:type

og:site_name
```

---

# Twitter Card

```
summary_large_image
```

kullanılacaktır.

---

# JSON-LD

Schema.org kullanılacaktır.

Kullanılacak yapılar

- Recipe
- BreadcrumbList
- Organization
- WebSite
- SearchAction
- ImageObject

---

# Breadcrumb

Her içerikte breadcrumb bulunmalıdır.

Örnek

```
Ana Sayfa

↓

Gaziantep

↓

Ali Nazik
```

---

# Heading Yapısı

Her sayfada yalnızca bir adet

```
H1
```

bulunmalıdır.

Sıralama

```
H1

H2

H3

H4
```

şeklinde olmalıdır.

Başlık seviyeleri atlanmamalıdır.

---

# İçerik Kalitesi

Her tarif;

- Özgün olmalıdır.
- Kopya içerik olmamalıdır.
- Yapay tekrar içermemelidir.
- Kullanıcıya gerçek değer sunmalıdır.

---

# Görseller

Her görsel

alt

özelliğine sahip olmalıdır.

Örnek

```
Alt

Ali Nazik Tarifi

Gaziantep Katmeri

Kayseri Mantısı
```

Dosya isimleri anlamlı olmalıdır.

```
ali-nazik.jpg

kayseri-mantisi.webp
```

---

# Görsel Optimizasyonu

WebP tercih edilir.

Lazy Loading kullanılmalıdır.

Responsive görseller kullanılmalıdır.

Gereksiz büyük dosyalar yüklenmez.

---

# Dahili Bağlantılar

İlgili içerikler birbirine bağlanmalıdır.

Örneğin

Tarif

↓

İl

↓

Kategori

↓

Malzeme

arasında bağlantılar kurulmalıdır.

---

# Sayfa Hızı

SEO için aşağıdaki hedefler uygulanacaktır.

Largest Contentful Paint

2.5 saniyenin altında.

Interaction to Next Paint

200 ms altında.

Cumulative Layout Shift

0.1 altında.

---

# Core Web Vitals

Google önerileri takip edilir.

Performans düzenli ölçülür.

---

# Mobil Uyumluluk

Mobil tasarım zorunludur.

Responsive olmayan sayfa yayınlanmaz.

---

# İç Linkleme

Her tarif en az aşağıdaki bağlantıları içermelidir.

- Aynı ildeki diğer tarifler
- Aynı kategorideki tarifler
- Benzer tarifler
- Aynı malzemeyi kullanan tarifler

---

# Dış Linkleme

Yalnızca güvenilir kaynaklara bağlantı verilir.

Sponsorlu bağlantılar uygun şekilde işaretlenir.

---

# Arama

Site içi arama indekslenebilir yapıda olacaktır.

Arama sonuçları filtrelenebilir olacaktır.

---

# 404 Sayfası

Özel tasarlanacaktır.

Kullanıcıya yönlendirme yapılacaktır.

---

# 301 Yönlendirmeleri

Slug değişirse

301 Redirect

kullanılacaktır.

---

# Çoklu Dil

Gelecekte

hreflang

etiketleri kullanılacaktır.

---

# Sosyal Medya

Her tarif paylaşılabilir olacaktır.

Open Graph ve Twitter Card eksiksiz kullanılacaktır.

---

# Sayfa Yapısı

Her tarif sayfasında aşağıdaki bilgiler bulunmalıdır.

- Başlık
- Açıklama
- Görsel
- Malzemeler
- Hazırlanış
- İl
- Bölge
- Kategori
- Etiketler
- Hazırlık Süresi
- Pişirme Süresi
- Porsiyon
- Kalori
- Puan
- Yorumlar

---

# Yapısal Veri

Recipe Schema aşağıdaki alanları içermelidir.

- name
- image
- description
- author
- prepTime
- cookTime
- totalTime
- recipeYield
- recipeIngredient
- recipeInstructions
- nutrition
- aggregateRating

---

# İndeksleme

İndekslenmeyecek sayfalar

- Admin
- Login
- Register
- Password Reset
- Profil Düzenleme
- Arama Parametreleri
- Filtre URL'leri

---

# Analiz Araçları

Production ortamında kullanılacaktır.

- Google Search Console
- Google Analytics 4
- Bing Webmaster Tools
- Microsoft Clarity

---

# Performans Takibi

Düzenli olarak kontrol edilir.

- Lighthouse
- PageSpeed Insights
- Core Web Vitals

---

# SEO Kontrol Listesi

Her yeni sayfada kontrol edilir.

- Benzersiz Title
- Benzersiz Description
- H1 mevcut
- Canonical mevcut
- Open Graph mevcut
- Twitter Card mevcut
- JSON-LD mevcut
- Breadcrumb mevcut
- Alt etiketleri mevcut
- Lazy Loading aktif
- Mobil uyumlu
- İç linkler mevcut
- Schema doğru
- Sitemap güncellendi

---

# Yasaklar

Aynı Title kullanmak.

Aynı Meta Description kullanmak.

Anahtar kelime doldurma (Keyword Stuffing).

Kopya içerik.

Alt etiketsiz görsel kullanmak.

Canonical kullanmamak.

H1'i birden fazla kullanmak.

Anlamsız URL oluşturmak.

Büyük görseller yüklemek.

JavaScript ile oluşturulan kritik SEO içeriği kullanmak.

Noindex olması gereken sayfaları indekslemek.

SEO kurallarını sonradan eklemeye çalışmak.