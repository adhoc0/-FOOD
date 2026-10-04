from datetime import datetime
from typing import cast

from django.contrib.sitemaps import Sitemap
from django.db.models import QuerySet

from .models import Province


class ProvinceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self) -> QuerySet[Province]:
        return cast(QuerySet[Province], Province.objects.active())

    def lastmod(self, obj: Province) -> datetime:
        return obj.updated_at
