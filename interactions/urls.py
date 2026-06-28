from django.urls import path
from .views import add_comment, toggle_favorite

app_name = 'interactions'

urlpatterns = [
    path('yorum-ekle/<int:recipe_id>/', add_comment, name='add_comment'),
    path('favori-degistir/<int:recipe_id>/', toggle_favorite, name='toggle_favorite'),
]
