---
name: postgresql
description: PostgreSQL geliştirme kuralları ve veritabanı standartları.
---

# PostgreSQL

## Genel Kurallar

- Her zaman Django ORM kullan.
- Raw SQL yalnızca ORM ile yapılamayan durumlarda kullanılabilir.
- Performans gerekçesi olmadan Raw SQL yazma.
- Migration dosyalarını elle değiştirme.
- Migration geçmişini koru.
- Gereksiz migration oluşturma.

---

## Model Tasarımı

- Her model BigAutoField kullanmalıdır.
- verbose_name ve verbose_name_plural tanımlanmalıdır.
- ordering tanımlanmalıdır.
- Gereken alanlarda db_index kullanılmalıdır.
- Benzersiz alanlarda unique=True kullanılmalıdır.
- ForeignKey ilişkilerinde uygun on_delete davranışı seçilmelidir.
- Gereksiz nullable alan oluşturma.

---

## İlişkiler

- OneToMany için ForeignKey kullan.
- ManyToMany yalnızca gerçekten gerekiyorsa kullan.
- İlişkilerde related_name tanımla.
- Circular dependency oluşturmaktan kaçın.

---

## Performans

- select_related() kullan.
- prefetch_related() kullan.
- only() ve defer() gerektiğinde kullanılabilir.
- annotate() ve aggregate() ORM üzerinden tercih edilir.
- N+1 sorgularına izin verme.

---

## Güvenlik

- SQL Injection riskine karşı ORM kullan.
- Kullanıcı girdisini doğrudan sorguya ekleme.
- Raw SQL gerekiyorsa parametreli sorgu kullan.

---

## Migration

- Model onaylanmadan migration oluşturma.
- Migration dosyalarını gereksiz yere silme.
- Production ortamında migration geçmişini değiştirme.
- Data Migration gerekiyorsa RunPython kullan.

---

## İndeksler

- Slug alanlarını indeksle.
- ForeignKey alanlarını değerlendir.
- Sık filtrelenen alanları indeksle.
- Gereksiz indeks oluşturma.

---

## Transaction

- İş kurallarında transaction.atomic() kullan.
- Birden fazla tabloyu değiştiren işlemler transaction içinde olmalıdır.

---

## Kod Kalitesi

- Business Logic modellerde bulunmamalıdır.
- İş kuralları Service katmanında olmalıdır.
- Karmaşık sorgular Selector katmanında olmalıdır.
- Validator'lar yalnızca doğrulama yapmalıdır.

---

## Yasaklar

- SELECT *
- Raw SQL (zorunlu olmadıkça)
- Gereksiz migration
- Hardcoded ID
- Gereksiz nullable alan
- N+1 sorgu