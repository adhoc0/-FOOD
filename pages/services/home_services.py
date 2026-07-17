from __future__ import annotations

from django.contrib.auth import get_user_model

from provinces.models import Province
from recipes.models import Category, Recipe


class HomePageService:
    """Service responsible for homepage data."""

    @staticmethod
    def get_context() -> dict:
        """Build homepage context."""

        return {
            "featured_recipes": (
                Recipe.objects
                .published_with_related()
                .featured()
                .recent()[:8]
            ),
            "latest_recipes": (
                Recipe.objects
                .published_with_related()
                .recent()[:12]
            ),
            "popular_recipes": (
                Recipe.objects
                .published_with_related()
                .popular()[:8]
            ),
            "categories": (
                Category.objects
                .active_with_recipe_count()
            ),
            "popular_provinces": (
                Province.objects
                .active_with_recipe_count()
                .order_by("-recipe_count", "name")[:8]
            ),
            "total_recipes": (
                Recipe.objects
                .published()
                .count()
            ),
            "total_categories": (
                Category.objects
                .active()
                .count()
            ),
            "total_provinces": (
                Province.objects
                .active()
                .count()
            ),
            "total_users": (
                get_user_model()
                .objects.active()
                .count()
            ),
        }
