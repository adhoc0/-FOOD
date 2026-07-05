from django.db import models
from django.urls import reverse


class Region(models.Model):
    """
    Türkiye'nin coğrafi bölgelerini temsil eder.
    """

    name = models.CharField(
        verbose_name="Bölge Adı",
        max_length=50,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name="Slug",
        max_length=60,
        unique=True,
        db_index=True,
    )

    description = models.TextField(
        verbose_name="Açıklama",
        blank=True,
    )

    map_color = models.CharField(
        verbose_name="Harita Rengi",
        max_length=7,
        default="#2E7D32",
        help_text="HEX formatında renk kodu (#RRGGBB).",
    )

    display_order = models.PositiveSmallIntegerField(
        verbose_name="Gösterim Sırası",
        default=1,
        db_index=True,
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
        verbose_name = "Bölge"
        verbose_name_plural = "Bölgeler"

        ordering = [
            "display_order",
            "name",
        ]

        indexes = [
            models.Index(fields=["display_order"]),
            models.Index(fields=["is_active"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "provinces:region_detail",
            kwargs={"slug": self.slug},
        )