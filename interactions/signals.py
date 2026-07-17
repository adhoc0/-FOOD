from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from interactions.models import Rating
from recipes.services.rating_service import RatingService


@receiver(post_save, sender=Rating)
@receiver(post_delete, sender=Rating)
def rating_changed(sender, instance, **kwargs):
    """Automatically update cached recipe rating stats when a rating changes."""
    RatingService._refresh_recipe_rating(instance.recipe)
