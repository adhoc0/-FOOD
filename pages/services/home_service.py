from __future__ import annotations

from provinces.selectors import ProvinceSelector
from recipes.selectors import CategorySelector, RecipeSelector


class HomePageService:
    """Homepage business logic."""

    @staticmethod
    def get_context() -> dict:
        return {
            "featured_recipes": RecipeSelector.get_featured_recipes(),
            "latest_recipes": RecipeSelector.get_latest_recipes(),
            "popular_provinces": ProvinceSelector.get_popular(),
            "categories": CategorySelector.get_all(),
            "total_recipes": RecipeSelector.get_recipe_count(),
            "total_provinces": ProvinceSelector.get_count(),
            "total_categories": CategorySelector.get_count(),
        }