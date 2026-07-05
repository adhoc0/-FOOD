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
