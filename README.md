# Türkiye Lezzet Haritası (Turkish Cuisine Map) 🍽️

Türkiye'nin dört bir yanından, 81 ilimize ait yöresel yemek tariflerini keşfedebileceğiniz, kendi tariflerinizi paylaşabileceğiniz ve diğer lezzet tutkunlarıyla etkileşime geçebileceğiniz interaktif bir web platformu.

## 🌟 Proje Özellikleri

- **İnteraktif Türkiye Haritası:** Ana sayfadaki SVG tabanlı dinamik harita üzerinden dilediğiniz ile tıklayarak o yörenin lezzetlerine anında ulaşabilirsiniz.
- **Kullanıcı Etkileşimleri:** 
  - Tariflere yıldızlı puan verme ve yorum yapma.
  - Beğenilen tarifleri favorilere ekleme ve profil sayfasında listeleme.
- **Topluluk Katkısı (UGC):** Üyelerin kendi yöresel tariflerini sisteme gönderebilmesi. Gönderilen tarifler, özel malzeme ayrıştırma algoritmasıyla otomatik formatlanır ve yönetici onayından sonra yayınlanır.
- **Gelişmiş Arama:** Yemek adı, açıklaması veya ait olduğu ile göre detaylı arama yapabilme.
- **Modern Arayüz:** *Glassmorphism* tasarım trendiyle harmanlanmış şeffaf, derinlikli ve karanlık tema (Dark Mode) hissiyatı veren şık kullanıcı deneyimi.

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python, Django 5.x
- **Veritabanı:** PostgreSQL
- **Frontend:** HTML5, Modern CSS (CSS Variables, Grid, Flexbox), Vanilla JavaScript
- **Görsellik:** FontAwesome (İkonlar), Inter Font, Özel Tasarım UI Bileşenleri
- **Deployment:** Docker, Docker Compose, Gunicorn, Nginx

## 📂 Proje Yapısı

Proje, S.O.L.I.D. prensiplerine uygun, sayfa bazlı ayrıştırılmış ve temiz kod anlayışıyla inşa edilmiştir:

- `core/`: Django temel ayarları, URL yapılandırması ve WSGI/ASGI ayarları.
- `accounts/`: Özel Kullanıcı Modeli (Custom User), Kayıt, Giriş, Şifre Sıfırlama ve Profil yönetimi.
- `recipes/`: Tarif yönetimi, arama, listeleme ve "Tarif Gönder" modülü.
- `provinces/`: İl bazlı kategori işlemleri (illerin detay sayfaları).
- `interactions/`: Yorum yapma, puanlama ve favoriye ekleme mantığı.
- `static/css/pages/`: Her sayfanın (`home.css`, `recipes.css`, `accounts.css`) kendine has stillerini barındıran CSS mimarisi.

## 🚀 Kurulum (Lokal Geliştirme)

1. Depoyu klonlayın ve klasöre girin:
   ```bash
   git clone <repo-url>
   cd FOOD
   ```
2. Sanal ortamı oluşturun ve bağımlılıkları yükleyin:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows için: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. PostgreSQL veritabanını oluşturun ve `.env` (veyahut `settings.py`) içerisine bağlantı bilgilerinizi girin.
4. Migrations ve statik dosyaları toplayın:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Sunucuyu çalıştırın:
   ```bash
   python manage.py runserver
   ```

## 🐳 Docker ile Canlıya Alım (Production)

Sunucunuzda tek tuşla projeyi ayağa kaldırmak için:

```bash
docker-compose up --build -d
```
Sistem;
1. `Gunicorn` WSGI sunucusunu çalıştırır.
2. `PostgreSQL` veritabanını bağlar.
3. `Nginx` üzerinden `80` portunu açarak hem reverse proxy yapar hem de statik/medya dosyalarını servis eder.

---

*Afiyet olsun!* 👩‍🍳👨‍🍳
