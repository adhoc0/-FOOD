from __future__ import annotations

from django.urls import path

from .views import (
    ProvinceDetailView,
    ProvinceListView,
)

app_name = "provinces"

urlpatterns = [
    path(
        "",
        ProvinceListView.as_view(),
        name="list",
    ),
    path(
        "<slug:slug>/",
        ProvinceDetailView.as_view(),
        name="detail",
    ),
]
