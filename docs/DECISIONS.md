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