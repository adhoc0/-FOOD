from django.db import models
from django.utils.text import slugify

class Ingredient(models.Model):
    """
    Malzemeler (Örn: Un, Şeker, Domates).
    """
    name = models.CharField('Malzeme Adı', max_length=100, unique=True)
    slug = models.SlugField('URL Uzantısı', max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'Malzeme'
        verbose_name_plural = 'Malzemeler'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            tr_map = str.maketrans('çğıöşüÇĞIÖŞÜ', 'cgiosuCGIOSU')
            mapped_name = self.name.translate(tr_map)
            self.slug = slugify(mapped_name)
        super().save(*args, **kwargs)
