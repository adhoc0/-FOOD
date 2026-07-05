from django.db import models
from .recipe import Recipe
from .ingredient import Ingredient

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
