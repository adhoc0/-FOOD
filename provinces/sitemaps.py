from django.contrib.sitemaps import Sitemap

from .models import Province


class ProvinceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Province.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at