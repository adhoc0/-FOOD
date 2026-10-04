---
title: Obsidian Vault Kullanım Rehberi
tags:
  - obsidian
  - guide
  - vault
  - wikilinks
date: 2026-09-28
---

# 🔮 Obsidian Vault Kullanım Rehberi

Bu Obsidian Kasası (Vault), FOOD projesinin tüm mimari, teknik ve süreç detaylarını birbiriyle ilişkili dinamik bir bilgi ağı halinde sunmak üzere tasarlanmıştır.

---

## 🧭 İpuçları ve En İyi Uygulamalar

### 1. WikiLink (`[[Bağlantı]]`) Gezintisi
- Herhangi bir nota tıklamak veya `Ctrl + Tıklama` yapmak o konunun detay notuna gitmenizi sağlar.
- `[[00 - HOME (MOC)]]` ana gezinti haritanızdır. Her an bu haritaya dönebilirsiniz.

### 2. Graph View (İlişki Ağı Görünümü)
- Sol menüden **Graph View** (İlişki Grafiği) ikonuna tıklayarak projedeki tüm modüllerin, kuralların ve mimari kararların birbiriyle nasıl bağlantılı olduğunu görselleştirebilirsiniz.
- Renk kodlaması için `#architecture`, `#security`, `#database`, `#app-module` etiketlerini filtre olarak kullanabilirsiniz.

### 3. Backlinks (Geri Bağlantılar) Pane
- Sağ panelde **Backlinks** sekmesini açarak, görüntülemekte olduğunuz notun projedeki hangi diğer notlar tarafından referans gösterildiğini anında görebilirsiniz.

### 4. Hızlı Arama (`Ctrl + O` veya `Ctrl + Shift + F`)
- `Ctrl + O` ile hızlıca not isimleri arasında arama yapabilir, `Ctrl + Shift + F` ile tüm kasanın içeriğinde tam metin araması yapabilirsiniz.

---

## 📁 Kasa Dizin Yapısı

```
food/
├── .obsidian/                       # Obsidian konfigürasyonu
├── 00 - HOME (MOC).md              # Ana Harita ve Navigasyon
├── 01 - Proje Genel/                # Proje Vizyonu, Roadmap, Changelog
├── 02 - Mimari ve Standartlar/      # Clean Architecture, PEP8, Güvenlik, SEO
├── 03 - Uygulama Modülleri/        # Django Uygulama Detayları (Accounts, Recipes vb.)
├── 04 - Veritabanı ve Şema/        # PostgreSQL Mimarisi, ERD Diyagramı
├── 05 - Deployment ve DevOps/       # Docker, Nginx, Production Checklist
└── 06 - Geliştirici Notları/        # ADR Kayıtları, Test Stratejisi, Rehber
```

---

## 🔗 İlgili Bağlantılar
- [[00 - HOME (MOC)]] — Ana Gezinti Haritası
- [[Clean Architecture]] — Mimari katman yapısı
