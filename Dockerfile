FROM python:3.12-slim

# Ortam değişkenlerini ayarla
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=/app

WORKDIR $HOME

# Sistem bağımlılıklarını kur (PostgreSQL için gerekli)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Bağımlılıkları kopyala ve kur
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Entrypoint betiğini kopyala ve çalıştırılabilir yap
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Media ve staticfiles klasörleri için izinleri ayarla
RUN mkdir -p /app/staticfiles /app/media
RUN chown -R www-data:www-data /app/staticfiles /app/media

# Başlangıç betiğini belirle
ENTRYPOINT ["/entrypoint.sh"]
