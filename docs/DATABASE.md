# DATABASE

## Amaç

Bu doküman projenin veritabanı mimarisini, kurallarını ve standartlarını tanımlar.

Veritabanı tasarımı;

- Güvenli
- Performanslı
- Ölçeklenebilir
- Normalize
- Bakımı kolay

olmalıdır.

---

# Veritabanı

Veritabanı Sistemi

PostgreSQL

Minimum Sürüm

PostgreSQL 16

Karakter Seti

UTF-8

Timezone

UTC

---

# Tasarım Prensipleri

Veritabanı mümkün olduğunca normalize edilmelidir.

Gereksiz veri tekrarına izin verilmez.

İlişkiler açık şekilde tanımlanmalıdır.

Primary Key olarak BigAutoField kullanılacaktır.

UUID yalnızca gerektiğinde kullanılacaktır.

Foreign Key ilişkileri bilinçli seçilecektir.

ManyToMany ilişkilerinde gerektiğinde ara tablo kullanılacaktır.

---

# İsimlendirme Kuralları

## Tablolar

Çoğul isim kullanılmaz.

Doğru

```
recipe
province
category
ingredient
user_profile
```

Yanlış

```
recipes
categories
provinces
```

---

## Alanlar

snake_case kullanılacaktır.

Doğru

```
created_at

updated_at

average_rating

image_url
```

---

## Foreign Key

```
province

category

recipe

user
```

şeklinde tanımlanacaktır.

---

## Tarih Alanları

Her tabloda mümkün olduğunca bulunmalıdır.

```
created_at

updated_at
```

---

# Primary Key

Her tabloda

```
BigAutoField
```

kullanılacaktır.

---

# Index Kuralları

Index kullanılmalıdır.

Özellikle;

Slug

ForeignKey

created_at

updated_at

plate_code

name

gibi alanlarda.

---

# Constraint Kuralları

Unique Constraint kullanılmalıdır.

Örneğin

```
Slug

Plate Code

E-mail

Username
```

Check Constraint kullanılmalıdır.

Örneğin

```
Puan

1-5
```

---

# Foreign Key Kuralları

Silme davranışı bilinçli seçilecektir.

```
CASCADE

PROTECT

SET_NULL

RESTRICT
```

gerektiği yerde kullanılacaktır.

Varsayılan olarak CASCADE kullanılmaz.

Her ilişki tek tek değerlendirilir.

---

# Transaction Kuralları

Birden fazla tabloyu etkileyen işlemler

```
transaction.atomic()
```

içerisinde yapılacaktır.

---

# ORM Kullanımı

Django ORM kullanılacaktır.

Raw SQL yalnızca gerçekten gerekli olduğunda kullanılacaktır.

---

# Query Kuralları

N+1 sorgularına izin verilmez.

Her sorgu optimize edilmelidir.

Kullanılması gerekenler

```
select_related()

prefetch_related()

only()

defer()

annotate()

aggregate()

exists()
```

---

# Pagination

Listeleme yapılan her sayfada pagination kullanılacaktır.

Tüm kayıtlar tek seferde çekilmeyecektir.

---

# Soft Delete

Soft Delete kullanılmayacaktır.

Silinmesi gereken veriler gerçekten silinecektir.

Gerekirse ayrı Archive tabloları kullanılacaktır.

---

# Slug Politikası

SEO amacıyla

Slug alanları benzersiz olacaktır.

Slug otomatik üretilecektir.

Slug değiştirilmeyecektir.

---

# Dosya Yönetimi

Dosya yolları veritabanında tutulacaktır.

Dosyanın kendisi veritabanında tutulmayacaktır.

---

# Görseller

Görseller

MEDIA_ROOT

üzerinde saklanacaktır.

Veritabanında yalnızca;

```
dosya yolu

alt metin

başlık

boyut

oluşturulma tarihi
```

saklanacaktır.

---

# JSON Kullanımı

JSONField yalnızca gerçekten gerekli olduğunda kullanılacaktır.

Normal ilişkiler yerine JSON kullanılmayacaktır.

---

# Null Politikası

Null mümkün olduğunca kullanılmayacaktır.

Boş string ile NULL birbirine karıştırılmayacaktır.

---

# Varsayılan Değerler

Her alanın anlamlı varsayılan değeri olmalıdır.

Anlamsız default değer kullanılmaz.

---

# Boolean Alanlar

Boolean alanlar açık isimlendirilmelidir.

Doğru

```
is_active

is_deleted

is_verified

is_featured

is_approved
```

---

# Sayısal Alanlar

Doğru veri tipi seçilmelidir.

```
PositiveIntegerField

PositiveSmallIntegerField

DecimalField

BigIntegerField
```

gerektiği yerde kullanılacaktır.

---

# Decimal Kullanımı

Para

Puan

Ortalama

gibi alanlarda

Float kullanılmaz.

DecimalField kullanılacaktır.

---

# CharField

Maksimum uzunluk bilinçli seçilmelidir.

255 varsayılan olarak kullanılmaz.

---

# TextField

Uzun içerikler için kullanılacaktır.

---

# ManyToMany

ManyToMany gerektiğinde

through

kullanılarak ara tablo oluşturulacaktır.

---

# Recipe Sistemi

Recipe

Category

Ingredient

Tag

Cuisine

Province

ilişkileri normalize olacaktır.

Tekrarlayan veri tutulmayacaktır.

---

# Kullanıcı Sistemi

User modeli mümkün olduğunca sade tutulacaktır.

Profil bilgileri ayrı tabloda tutulacaktır.

---

# Favoriler

Favoriler ayrı tabloda tutulacaktır.

Tekrar eden kayıt oluşturulmayacaktır.

Unique Constraint kullanılacaktır.

---

# Puanlama

Bir kullanıcı aynı tarife yalnızca bir kez puan verebilir.

Unique Constraint kullanılacaktır.

---

# Yorumlar

Yorumlar ayrı tabloda tutulacaktır.

Admin onayı desteklenecektir.

---

# Arama

Arama için PostgreSQL Full Text Search kullanılacaktır.

Gelecekte Elasticsearch desteği planlanmaktadır.

---

# Cache

Sık kullanılan sorgular cache'e alınacaktır.

---

# Migration Kuralları

Migration dosyaları düzenlenmez.

Yeni migration oluşturulur.

Migration silinmez.

Production ortamında migration geri alınmaz.

---

# Backup

Günlük otomatik yedek alınacaktır.

Yedekler şifreli saklanacaktır.

Düzenli geri yükleme testleri yapılacaktır.

---

# Güvenlik

SQL Injection koruması zorunludur.

Raw SQL minimum seviyede kullanılacaktır.

Kullanıcı girdileri doğrulanacaktır.

Veritabanı erişimi yetkilendirilecektir.

---

# Performans

Büyük tablolar için index kullanılacaktır.

Sorgular EXPLAIN ANALYZE ile test edilecektir.

Gereksiz join yapılmayacaktır.

Toplu işlemlerde

```
bulk_create()

bulk_update()
```

tercih edilecektir.

---

# Veri Bütünlüğü

Foreign Key kullanılmalıdır.

Constraint kullanılmalıdır.

Duplicate kayıt oluşmasına izin verilmez.

Silinen ilişkiler kontrol edilmelidir.

---

# Ölçeklenebilirlik

Veritabanı yüz binlerce kullanıcı ve on binlerce tarifi destekleyecek şekilde tasarlanacaktır.

Performans geçici çözümlerle değil, doğru veri modeli ve doğru indeksleme ile sağlanacaktır.

---

# Yasaklar

Raw SQL kullanmak (zorunlu olmadıkça).

Indexsiz büyük sorgular yazmak.

N+1 sorguları oluşturmak.

Float kullanmak (para veya puan için).

Magic Number kullanmak.

Gereksiz NULL alanlar oluşturmak.

Dosyaları veritabanında saklamak.

Migration dosyalarını manuel değiştirmek.

Tekrarlayan veri saklamak.

İlişki yerine JSON kullanmak.

Constraint kullanılması gereken yerde kullanmamak.