from django.db import models
from django.urls import reverse

from .region import Region


class Province(models.Model):
    """
    Türkiye'deki illeri temsil eder.
    """

    region = models.ForeignKey(
        Region,
        verbose_name="Bölge",
        on_delete=models.PROTECT,
        related_name="provinces",
    )

    plate_code = models.PositiveSmallIntegerField(
        verbose_name="Plaka Kodu",
        unique=True,
        db_index=True,
    )

    name = models.CharField(
        verbose_name="İl Adı",
        max_length=100,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name="Slug",
        max_length=120,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        verbose_name="Açıklama",
        blank=True,
    )

    latitude = models.DecimalField(
        verbose_name="Enlem",
        max_digits=9,
        decimal_places=6,
    )

    longitude = models.DecimalField(
        verbose_name="Boylam",
        max_digits=9,
        decimal_places=6,
    )

    map_x = models.DecimalField(
        verbose_name="Harita X",
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    map_y = models.DecimalField(
        verbose_name="Harita Y",
        max_digits=8,
        decimal_places=2,
        default=0,
    )

    is_featured = models.BooleanField(
        verbose_name="Öne Çıkan",
        default=False,
    )

    is_active = models.BooleanField(
        verbose_name="Aktif",
        default=True,
        db_index=True,
    )

    created_at = models.DateTimeField(
        verbose_name="Oluşturulma Tarihi",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name="Güncellenme Tarihi",
        auto_now=True,
    )

    class Meta:
        verbose_name = "İl"
        verbose_name_plural = "İller"

        ordering = [
            "plate_code",
        ]

        indexes = [
            models.Index(fields=["region"]),
            models.Index(fields=["slug"]),
            models.Index(fields=["plate_code"]),
            models.Index(fields=["is_active"]),
            models.Index(fields=["region", "is_active"]),
        ]

    def __str__(self):
        return f"{self.plate_code:02d} - {self.name}"

    def get_absolute_url(self):
        return reverse(
            "provinces:province_detail",
            kwargs={
                "slug": self.slug,
            },
        )