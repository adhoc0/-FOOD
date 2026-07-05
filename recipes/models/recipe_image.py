from django.db import models
from .recipe import Recipe

class RecipeImage(models.Model):
    """
    Tarif görselleri.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Görsel', upload_to='recipes/%Y/%m/')
    alt_text = models.CharField('Alternatif Metin (SEO)', max_length=100)
    is_primary = models.BooleanField('Ana Görsel mi?', default=False)
    order = models.PositiveSmallIntegerField('Sıralama', default=0)

    class Meta:
        verbose_name = 'Tarif Görseli'
        verbose_name_plural = 'Tarif Görselleri'
        ordering = ['order', '-is_primary']

    def __str__(self):
        return f"{self.recipe.title} - Görsel {self.order}"
    
    def save(self, *args, **kwargs):
        # Eğer bu ana görsel seçildiyse, diğer ana görselleri iptal et
        if self.is_primary:
            RecipeImage.objects.filter(recipe=self.recipe, is_primary=True).exclude(pk=self.pk).update(is_primary=False)
        super().save(*args, **kwargs)
