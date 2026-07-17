from __future__ import annotations

from django.urls import path

from .views import (
    AboutPageView,
    ContactPageView,
    CookiesPageView,
    HomePageView,
    KVKKPageView,
    PrivacyPageView,
    TermsPageView,
)

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("hakkimizda/", AboutPageView.as_view(), name="about"),
    path("iletisim/", ContactPageView.as_view(), name="contact"),
    path("gizlilik-politikasi/",PrivacyPageView.as_view(),name="privacy",),
    path("kvkk/", KVKKPageView.as_view(), name="kvkk"),
    path("cerez-politikasi/",CookiesPageView.as_view(), name="cookies",),
    path("kullanim-sartlari/", TermsPageView.as_view(), name="terms"),
]
