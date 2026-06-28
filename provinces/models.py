from django.db import models
from django.utils.text import slugify


class Province(models.Model):
    """
    Türkiye'nin illeri.
    """
    REGION_CHOICES = (
        ('Marmara', 'Marmara Bölgesi'),
        ('Ege', 'Ege Bölgesi'),
        ('Akdeniz', 'Akdeniz Bölgesi'),
        ('İç Anadolu', 'İç Anadolu Bölgesi'),
        ('Karadeniz', 'Karadeniz Bölgesi'),
        ('Doğu Anadolu', 'Doğu Anadolu Bölgesi'),
        ('Güneydoğu Anadolu', 'Güneydoğu Anadolu Bölgesi'),
    )

    name = models.CharField('İl Adı', max_length=50, unique=True)
    slug = models.SlugField('URL Uzantısı', max_length=50, unique=True, blank=True)
    plate_code = models.PositiveSmallIntegerField('Plaka Kodu', unique=True)
    region = models.CharField('Bölge', max_length=20, choices=REGION_CHOICES)
    latitude = models.DecimalField('Enlem', max_digits=9, decimal_places=6)
    longitude = models.DecimalField('Boylam', max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = 'İl'
        verbose_name_plural = 'İller'
        ordering = ['plate_code']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            # Türkçe karakterleri düzgün çevirmek için replace
            tr_map = str.maketrans('çğıöşüÇĞIÖŞÜ', 'cgiosuCGIOSU')
            mapped_name = self.name.translate(tr_map)
            self.slug = slugify(mapped_name)
        super().save(*args, **kwargs)
