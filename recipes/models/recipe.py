from django.db import models
from django.utils.text import slugify

from provinces.models import Province

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
