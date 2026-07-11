# Django Scripts

## Amaç

Bu klasör Django geliştirme sürecinde kullanılan yardımcı scriptleri içerir.

Scriptler doğrudan proje kodunun parçası değildir.

Tekrarlanan işlemleri otomatikleştirmek amacıyla kullanılır.

---

# Script Türleri

## Veritabanı

- Backup
- Restore
- Reset
- Seed

---

## Migration

- Migration kontrolü
- Migration temizleme
- Migration raporu

---

## Fixtures

- Fixture oluşturma
- Fixture yükleme
- Fixture doğrulama

---

## Kullanıcı

- Superuser oluşturma
- Test kullanıcıları oluşturma

---

## Static

- collectstatic
- static temizleme

---

## Media

- Media temizleme
- Test dosyaları oluşturma

---

## Cache

- Cache temizleme
- Cache raporu

---

## Development

- Fake Data üretme
- Benchmark çalıştırma
- Test ortamı hazırlama

---

## Deployment

- Release kontrolü
- Build scriptleri
- Health Check

---

# Kurallar

- Scriptler idempotent olmalıdır.
- Production verisini silen script yazılmaz.
- Her script açıklama içermelidir.
- Her script tekrar çalıştırılabilir olmalıdır.
- Scriptler mümkün olduğunca platform bağımsız olmalıdır.

---

# Örnek Dosyalar

backup_database.py

restore_database.py

seed_regions.py

seed_provinces.py

create_superuser.py

reset_database.py

cleanup_media.py

health_check.py