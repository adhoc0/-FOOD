from django.urls import path, register_converter

from core.converters import UnicodeSlugConverter
from recipes.views import (
    CategoryDetailView,
    CategoryListView,
    RecipeDetailView,
    RecipeListView,
    SearchView,
)

app_name = "recipes"

register_converter(UnicodeSlugConverter, "unicode_slug")

urlpatterns = [
    path(
        "",
        RecipeListView.as_view(),
        name="list",
    ),
    path(
        "ara/",
        SearchView.as_view(),
        name="search",
    ),
    path(
        "kategori/",
        CategoryListView.as_view(),
        name="category_list",
    ),
    path(
        "kategori/<unicode_slug:slug>/",
        CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "<unicode_slug:slug>/",
        RecipeDetailView.as_view(),
        name="recipe_detail",
    ),
]
