"""
Search views.

Recipe search and filtering.
"""

from __future__ import annotations

from django.views.generic import ListView

from provinces.models import Province
from recipes.choices import Difficulty
from recipes.constants import SEARCH_PAGE_SIZE
from recipes.models import Category, Recipe
from recipes.services import SearchService


class SearchView(ListView):
    """Recipe search view."""

    model = Recipe
    template_name = "recipes/search.html"
    context_object_name = "recipes"
    paginate_by = SEARCH_PAGE_SIZE

    def get_queryset(self):
        self.query = self.request.GET.get(
            "q",
            "",
        ).strip()

        self.province_slug = self.request.GET.get(
            "province",
            "",
        ).strip()

        self.category_slug = self.request.GET.get(
            "category",
            "",
        ).strip()

        self.difficulty = self.request.GET.get(
            "difficulty",
            "",
        ).strip()

        self.ordering = self.request.GET.get(
            "sort",
            "",
        ).strip()

        queryset = SearchService.search_recipes(
            query=self.query,
        )

        if self.province_slug:
            queryset = queryset.filter(
                province__slug=self.province_slug,
            )

        if self.category_slug:
            queryset = queryset.filter(
                category__slug=self.category_slug,
            )

        if self.difficulty:
            queryset = queryset.filter(
                difficulty=self.difficulty,
            )

        ordering_map = {
            "latest": [
                "-published_at",
                "-created_at",
            ],
            "oldest": [
                "published_at",
                "created_at",
            ],
            "popular": [
                "-view_count",
                "-favorite_count",
            ],
            "rating": [
                "-average_rating",
                "-rating_count",
            ],
            "favorites": [
                "-favorite_count",
            ],
            "title": [
                "title",
            ],
        }

        return queryset.order_by(
            *ordering_map.get(
                self.ordering,
                [
                    "-published_at",
                    "-created_at",
                ],
            ),
        )

    def get_context_data(
        self,
        **kwargs,
    ):
        context = super().get_context_data(**kwargs)

        context["query"] = self.query
        context["current_province"] = self.province_slug
        context["current_category"] = self.category_slug
        context["current_difficulty"] = self.difficulty
        context["current_sort"] = self.ordering

        context["provinces"] = (
            Province.objects.filter(
                is_active=True,
            )
            .order_by(
                "name",
            )
            .values(
                "name",
                "slug",
            )
        )

        context["categories"] = (
            Category.objects.filter(
                is_active=True,
            )
            .order_by(
                "name",
            )
            .values(
                "name",
                "slug",
            )
        )

        context["difficulties"] = Difficulty.choices

        context["total_results"] = self.get_queryset().count()

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
