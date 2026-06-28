from django.urls import path
from .views import RecipeDetailView, RecipeListView, RecipeCreateView

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='list'),
    path('yeni/', RecipeCreateView.as_view(), name='create'),
    path('<slug:slug>/', RecipeDetailView.as_view(), name='detail'),
]
