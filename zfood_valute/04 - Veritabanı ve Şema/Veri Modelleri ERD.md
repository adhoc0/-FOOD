---
title: Veri Modelleri ve ERD Şeması
tags:
  - database
  - erd
  - mermaid
  - models
date: 2026-09-28
---

# 📊 Veri Modelleri ve ERD Şeması

Aşağıdaki Mermaid ERD diyagramı, FOOD platformundaki temel modelleri ve aralarındaki veritabanı ilişkilerini göstermektedir.

---

## 📐 ERD Diyagramı (Entity Relationship Diagram)

```mermaid
erDiagram
    User ||--o{ Recipe : "yazarıdır (SET_NULL)"
    User ||--o{ Favorite : "favoriye ekler (CASCADE)"
    User ||--o{ Rating : "puan verir (CASCADE)"
    User ||--o{ Comment : "yorum yapar (CASCADE)"
    
    Region ||--o{ Province : "içerir (PROTECT)"
    Province ||--o{ Recipe : "ait olduğu il (PROTECT)"
    Category ||--o{ Recipe : "kategorisidir (PROTECT)"
    Cuisine ||--o{ Recipe : "mutfak türü (SET_NULL)"
    
    Recipe ||--o{ RecipeImage : "görselleri (CASCADE)"
    Recipe ||--o{ RecipeIngredient : "malzemeleri (CASCADE)"
    Ingredient ||--o{ RecipeIngredient : "kullanıldığı tarifler (PROTECT)"
    
    Recipe ||--o{ Favorite : "favorilenir (CASCADE)"
    Recipe ||--o{ Rating : "puanlanır (CASCADE)"
    Recipe ||--o{ Comment : "yorumlanır (CASCADE)"

    User {
        bigint id PK
        string email UK
        string username UK
        string bio
        boolean is_verified
    }

    Region {
        bigint id PK
        string name
        string slug UK
        boolean is_active
    }

    Province {
        bigint id PK
        string name UK
        int plate_code UK
        bigint region_id FK
        string slug UK
    }

    Recipe {
        bigint id PK
        string title
        string slug UK
        bigint province_id FK
        bigint category_id FK
        bigint cuisine_id FK
        bigint author_id FK
        int prep_time_minutes
        int cook_time_minutes
        boolean is_featured
        boolean is_approved
    }

    Rating {
        bigint id PK
        bigint user_id FK
        bigint recipe_id FK
        int score "CheckConstraint 1-5"
    }

    Favorite {
        bigint id PK
        bigint user_id FK
        bigint recipe_id FK
    }

    Comment {
        bigint id PK
        bigint user_id FK
        bigint recipe_id FK
        text content
        boolean is_approved
    }
```

---

## 🔗 Modül Detayları
- [[Accounts Modülü]] — `User` tablosu detayları
- [[Provinces Modülü]] — `Region` ve `Province` tabloları
- [[Recipes Modülü]] — `Recipe`, `Category`, `Ingredient`, `RecipeImage` tabloları
- [[Interactions Modülü]] — `Rating`, `Favorite`, `Comment` tabloları
