from __future__ import annotations

from django.http import Http404
from django.views.generic import ListView

from recipes.constants import DEFAULT_PAGE_SIZE
from recipes.models import Category, Recipe
from recipes.selectors import CategorySelector


class CategoryListView(ListView):
    """List active categories."""

    model = Category
    template_name = "recipes/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return CategorySelector.get_all_active()


class CategoryDetailView(ListView):
    """Display published recipes for a category."""

    model = Recipe
    template_name = "recipes/category_detail.html"
    context_object_name = "recipes"
    paginate_by = DEFAULT_PAGE_SIZE

    def get_category(self) -> Category:
        category = CategorySelector.get_by_slug(self.kwargs["slug"])

        if category is None:
            raise Http404("Category not found.")

        return category

    def get_queryset(self):
        self.category = self.get_category()
        _, recipes = CategorySelector.get_published_recipes(self.category.slug)
        return recipes

    def get_context_data(
        self,
        **kwargs,
    ):
        context = super().get_context_data(**kwargs)

        category = self.category

        context["category"] = category
        context["recipe_count"] = context["paginator"].count

        context["meta_title"] = (
            f"{category.name} Tarifleri | Türkiye Yöresel Yemekleri"
        )

        context["meta_description"] = (
            category.description[:160]
            if category.description
            else f"{category.name} kategorisindeki yöresel yemek tarifleri."
        )

        context["breadcrumbs"] = [
            {
                "title": "Ana Sayfa",
                "url": "/",
            },
            {
                "title": "Kategoriler",
                "url": "/recipes/categories/",
            },
            {
                "title": category.name,
                "url": "",
            },
        ]

        return context
