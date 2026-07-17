from django.conf import settings
from django.db import models

from recipes.models import Recipe


class Comment(models.Model):
    """
    Tarif yorumları. Admin onayından geçmesi gerekir.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField("Yorum")

    is_approved = models.BooleanField(
        "Onaylandı mı?",
        default=False,
        help_text="Yorum yayınlanmadan önce admin tarafından onaylanmalıdır.",
    )

    created_at = models.DateTimeField("Oluşturulma Tarihi", auto_now_add=True)
    updated_at = models.DateTimeField("Güncellenme Tarihi", auto_now=True)

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        ordering = ["-created_at"]

    def __str__(self):
        status = "Onaylı" if self.is_approved else "Bekliyor"
        return f"{self.user.username} - {self.recipe.title} [{status}]"
