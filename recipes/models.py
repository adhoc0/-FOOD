from django.db import models
from django.utils.text import slugify

from provinces.models import Province


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


class Recipe(models.Model):
    """
    Yemek Tarifleri.
    """
    DIFFICULTY_CHOICES = (
        ('Kolay', 'Kolay'),
        ('Orta', 'Orta'),
        ('Zor', 'Zor'),
    )

    title = models.CharField('Tarif Adı', max_length=200)
    slug = models.SlugField('URL Uzantısı', max_length=200, unique=True, blank=True)
    description = models.TextField('Kısa Açıklama')
    instructions = models.TextField('Yapılışı')
    
    prep_time_minutes = models.PositiveSmallIntegerField('Hazırlama Süresi (Dk)')
    cook_time_minutes = models.PositiveSmallIntegerField('Pişirme Süresi (Dk)')
    serving_size = models.PositiveSmallIntegerField('Kaç Kişilik')
    difficulty = models.CharField('Zorluk', max_length=10, choices=DIFFICULTY_CHOICES)
    
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='recipes', verbose_name='Ait Olduğu İl')
    
    # Meta fields
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True)
    is_published = models.BooleanField('Yayında mı?', default=True)
    
    # SEO
    meta_title = models.CharField('SEO Başlığı', max_length=60, blank=True, help_text='Boş bırakılırsa Tarif Adı kullanılır.')
    meta_description = models.CharField('SEO Açıklaması', max_length=160, blank=True, help_text='Boş bırakılırsa Kısa Açıklama kullanılır.')

    class Meta:
        verbose_name = 'Tarif'
        verbose_name_plural = 'Tarifler'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['province', 'is_published']),
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            tr_map = str.maketrans('çğıöşüÇĞIÖŞÜ', 'cgiosuCGIOSU')
            mapped_name = self.title.translate(tr_map)
            self.slug = slugify(mapped_name)
        
        # SEO alanları otomatik doldurma
        if not self.meta_title:
            self.meta_title = self.title[:60]
        if not self.meta_description:
            self.meta_description = self.description[:160]
            
        super().save(*args, **kwargs)


class RecipeIngredient(models.Model):
    """
    Bir tarifte kullanılan malzemeler ve miktarları (M2M through tablosu).
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='used_in_recipes')
    quantity = models.CharField('Miktar', max_length=50)
    unit = models.CharField('Birim', max_length=50, blank=True)
    order = models.PositiveSmallIntegerField('Sıralama', default=0)

    class Meta:
        verbose_name = 'Tarif Malzemesi'
        verbose_name_plural = 'Tarif Malzemeleri'
        ordering = ['order']
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        if self.unit:
            return f"{self.quantity} {self.unit} {self.ingredient.name}"
        return f"{self.quantity} {self.ingredient.name}"


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
