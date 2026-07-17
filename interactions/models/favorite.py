from django.conf import settings
from django.db import models

from recipes.models import Recipe


class Favorite(models.Model):
    """
    Kullanıcının favori tarifleri.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites"
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favorited_by")
    created_at = models.DateTimeField("Eklenme Tarihi", auto_now_add=True)

    class Meta:
        verbose_name = "Favori"
        verbose_name_plural = "Favoriler"
        # Bir kullanıcı aynı tarifi sadece 1 kez favorilere ekleyebilir
        unique_together = ("user", "recipe")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.recipe.title}"
