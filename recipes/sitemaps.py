from datetime import datetime
from typing import cast

from django.contrib.sitemaps import Sitemap
from django.db.models import QuerySet

from recipes.models import Recipe
from recipes.models.recipe import Status


class RecipeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self) -> QuerySet[Recipe]:
        return cast(
            QuerySet[Recipe],
            Recipe.objects.filter(
                status=Status.PUBLISHED,
                is_active=True,
            ).order_by("-published_at"),
        )

    def lastmod(self, obj: Recipe) -> datetime:
        return obj.updated_at
