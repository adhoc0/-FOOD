from django.db import models

from .recipe_queryset import RecipeQuerySet


class RecipeManager(models.Manager):
    """Recipe manager."""

    def get_queryset(self):
        return RecipeQuerySet(
            self.model,
            using=self._db,
        )

    def active(self):
        return self.get_queryset().active()

    def published(self):
        return self.get_queryset().published()

    def featured(self):
        return self.get_queryset().featured()

    def by_province(self, province):
        return self.get_queryset().by_province(
            province,
        )

    def by_category(self, category):
        return self.get_queryset().by_category(
            category,
        )

    def search(self, query: str):
        return self.get_queryset().search(
            query,
        )