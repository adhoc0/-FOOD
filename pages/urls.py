from django.urls import path


from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    PrivacyPolicyView,
    CookiePolicyView,
    TermsOfServiceView,
    KVKKPageView,
)

app_name = "pages"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("hakkimizda/", AboutPageView.as_view(), name="about"),
    path("iletisim/", ContactPageView.as_view(), name="contact"),
    path(
        "gizlilik-politikasi/",
        PrivacyPolicyView.as_view(),
        name="privacy",
    ),
    path(
        "cerez-politikasi/",
        CookiePolicyView.as_view(),
        name="cookies",
    ),
    path(
        "kullanim-kosullari/",
        TermsOfServiceView.as_view(),
        name="terms",
    ),
    path("kvkk/", KVKKPageView.as_view(), name="kvkk"),
]
