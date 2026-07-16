from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Q

from recipes.models import Recipe


class Rating(models.Model):
    """
    Tarif puanlaması (1-5 yıldız).
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ratings"
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ratings")
    score = models.PositiveSmallIntegerField(
        "Puan", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "Puan"
        verbose_name_plural = "Puanlar"
        # Bir kullanıcı bir tarife sadece 1 kez puan verebilir
        unique_together = ("user", "recipe")
        constraints = [
            models.CheckConstraint(
                condition=Q(score__gte=1, score__lte=5),
                name="rating_score_between_one_and_five",
            ),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title} ({self.score}/5)"
