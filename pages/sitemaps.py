from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticPageSitemap(Sitemap):
    protocol = "https"

    def items(self) -> list[str]:
        return [
            "pages:home",
            "pages:about",
            "pages:contact",
            "pages:privacy",
            "pages:cookies",
            "pages:kvkk",
            "pages:terms",
        ]

    def location(self, item: str) -> str:
        return reverse(item)

    def priority(self, item: str) -> float:
        if item == "pages:home":
            return 1.0
        return 0.8

    def changefreq(self, item: str) -> str:
        if item == "pages:home":
            return "daily"
        return "monthly"
