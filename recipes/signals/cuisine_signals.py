from typing import Any

from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.utils.slug import generate_slug
from recipes.models import Cuisine


@receiver(pre_save, sender=Cuisine)
def cuisine_pre_save(sender: Any, instance: Any, **kwargs: Any) -> None:
    if not instance.slug:
        instance.slug = generate_slug(
            instance.name,
        )
