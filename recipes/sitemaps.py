from django.contrib.sitemaps import Sitemap

from recipes.models import Recipe
from recipes.models.recipe import Status


class RecipeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Recipe.objects.filter(
            status=Status.PUBLISHED,
            is_active=True,
        ).order_by("-published_at")

    def lastmod(self, obj):
        return obj.updated_at
