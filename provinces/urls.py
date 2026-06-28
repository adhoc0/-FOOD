from django.urls import path
from .views import ProvinceDetailView

app_name = 'provinces'

urlpatterns = [
    path('il/<slug:slug>/', ProvinceDetailView.as_view(), name='province_detail'),
]
