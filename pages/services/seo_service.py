from __future__ import annotations


class SEOService:
    """SEO helper service."""

    @staticmethod
    def homepage() -> dict:
        return {
            "title": "Türkiye Yöresel Yemekleri",
            "description": (
                "Türkiye'nin 81 iline ait yöresel yemekleri, "
                "geleneksel tarifleri ve lezzet haritasını keşfedin."
            ),
        }