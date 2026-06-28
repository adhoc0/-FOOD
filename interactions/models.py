from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from recipes.models import Recipe


class Rating(models.Model):
    """
    Tarif puanlaması (1-5 yıldız).
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    score = models.PositiveSmallIntegerField(
        'Puan', 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)

    class Meta:
        verbose_name = 'Puan'
        verbose_name_plural = 'Puanlar'
        # Bir kullanıcı bir tarife sadece 1 kez puan verebilir
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title} ({self.score}/5)"


class Favorite(models.Model):
    """
    Kullanıcının favori tarifleri.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField('Eklenme Tarihi', auto_now_add=True)

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = 'Favoriler'
        # Bir kullanıcı aynı tarifi sadece 1 kez favorilere ekleyebilir
        unique_together = ('user', 'recipe')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"


class Comment(models.Model):
    """
    Tarif yorumları. Admin onayından geçmesi gerekir.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField('Yorum')
    
    is_approved = models.BooleanField(
        'Onaylandı mı?', 
        default=False,
        help_text='Yorum yayınlanmadan önce admin tarafından onaylanmalıdır.'
    )
    
    created_at = models.DateTimeField('Oluşturulma Tarihi', auto_now_add=True)
    updated_at = models.DateTimeField('Güncellenme Tarihi', auto_now=True)

    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ['-created_at']

    def __str__(self):
        status = "Onaylı" if self.is_approved else "Bekliyor"
        return f"{self.user.username} - {self.recipe.title} [{status}]"
