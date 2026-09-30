"""
Search views.

Recipe search and filtering.
"""

from __future__ import annotations

from django.views.generic import ListView

from provinces.selectors import ProvinceSelector
from recipes.choices import Difficulty
from recipes.constants import SEARCH_PAGE_SIZE
from recipes.models import Recipe
from recipes.selectors import CategorySelector, RecipeSelector


class SearchView(ListView):
    """Recipe search view."""

    model = Recipe
    template_name = "recipes/search.html"
    context_object_name = "recipes"
    paginate_by = SEARCH_PAGE_SIZE

    def get_queryset(self):
        self.query = self.request.GET.get("q", "").strip()
        self.province_slug = self.request.GET.get("province", "").strip()
        self.category_slug = self.request.GET.get("category", "").strip()
        self.difficulty = self.request.GET.get("difficulty", "").strip()
        self.ordering = self.request.GET.get("sort", "").strip()

        return RecipeSelector.search_published(
            query=self.query,
            province_slug=self.province_slug,
            category_slug=self.category_slug,
            difficulty=self.difficulty,
            ordering=self.ordering or "latest",
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["query"] = self.query
        context["current_province"] = self.province_slug
        context["current_category"] = self.category_slug
        context["current_difficulty"] = self.difficulty
        context["current_sort"] = self.ordering

        context["provinces"] = ProvinceSelector.get_active_list()
        context["categories"] = CategorySelector.get_all_active()

        context["difficulties"] = Difficulty.choices

        # Sayfalayıcı toplamı zaten hesapladığı için ikinci bir COUNT sorgusu yapılmaz.
        context["total_results"] = context["paginator"].count

        context["meta_title"] = (
            f'"{self.query}" Arama Sonuçları | Türkiye Yöresel Yemekleri'
            if self.query
            else "Tarif Ara | Türkiye Yöresel Yemekleri"
        )

        context["meta_description"] = (
            f'"{self.query}" için bulunan yöresel yemek tarifleri.'
            if self.query
            else "Türkiye'nin yöresel yemek tariflerini arayın."
        )

        return context
