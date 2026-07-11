from django.db import models
from django.db.models import Q

from recipes.models.recipe import Status


class RecipeQuerySet(models.QuerySet):
    """Custom queryset for Recipe."""

    def active(self):
        return self.filter(
            is_active=True,
        )

    def published(self):
        return self.active().filter(
            status=Status.PUBLISHED,
        )

    def featured(self):
        return self.published().filter(
            is_featured=True,
        )

    def by_province(self, province):
        return self.published().filter(
            province=province,
        )

    def by_category(self, category):
        return self.published().filter(
            category=category,
        )

    def search(self, query: str):
        return self.published().filter(
            Q(title__icontains=query)
            | Q(summary__icontains=query)
            | Q(province__name__icontains=query)
            | Q(category__name__icontains=query)
        )