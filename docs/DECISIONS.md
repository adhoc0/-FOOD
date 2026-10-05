# ADR-001

## Region modeli silinmeyecektir.

### Karar

Region kayıtları fiziksel olarak silinmeyecektir.

Yalnızca `is_active=False` yapılacaktır.

### Gerekçe

Region, Province ve Recipe modellerinin temel referans tablosudur.

Silinmesi veri bütünlüğünü bozabilir.

### Sonuç

Projede Region için fiziksel silme işlemi uygulanmayacaktır.
---

# ADR-002

## Favori ve puan servisleri `interactions` uygulamasına taşındı.

### Karar

`FavoriteService` ve `RatingService`, `recipes/services/` altından `interactions/services/`
altına taşındı. Artık `from interactions.services import FavoriteService, RatingService`
ile içe aktarılır; `recipes.services` bunları dışa aktarmaz.

### Gerekçe

`Favorite` ve `Rating` modelleri, `CommentService` ve bu işlemlerin view'ları zaten
`interactions` uygulamasındadır. Servislerin `recipes` içinde durması bağımlılık yönünü
tersine çeviriyordu (`recipes` → `interactions` modelleri). Her uygulama kendi modellerinin
iş kurallarına sahip olmalıdır.

### Sonuç

- Bağımlılık yönü tek: `interactions` → `recipes` (tarif modeli ve `RecipeService`
  sayaçları). `recipes` yalnızca detay görünümünde `interactions.services` okur.
- Davranış ve veritabanı değişmedi; yalnızca modül yolu değişti.
- Eski yol (`recipes.services.FavoriteService`) için uyumluluk katmanı bırakılmadı;
  proje içi tek kullanıcıydı.
