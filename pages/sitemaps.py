from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticPageSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return [
            "pages:home",
            "pages:about",
            "pages:contact",
            "pages:privacy",
            "pages:cookies",
            "pages:kvkk",
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == "pages:home":
            return 1.0
        return 0.8

    def changefreq(self, item):
        if item == "pages:home":
            return "daily"
        return "monthly"
