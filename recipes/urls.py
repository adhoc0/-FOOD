from django.urls import path

from .views import (RecipeCreateView, RecipeDetailView, RecipeListView,
)

app_name = "recipes"

urlpatterns = [
    path("", RecipeListView.as_view(),name="list",),
    path("olustur/", RecipeCreateView.as_view(),name="create",),
    path("<slug:slug>/", RecipeDetailView.as_view(),name="detail",),
]