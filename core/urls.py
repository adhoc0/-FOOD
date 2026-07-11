from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from pages.sitemaps import StaticPageSitemap
from provinces.sitemaps import ProvinceSitemap
from recipes.sitemaps import RecipeSitemap

admin.site.site_header = "Türkiye Yöresel Yemekleri — Yönetim"
admin.site.site_title = "Lezzet Haritası Admin"
admin.site.index_title = "Yönetim Paneli"

sitemaps = {
    "pages": StaticPageSitemap,
    "provinces": ProvinceSitemap,
    "recipes": RecipeSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("pages.urls")),
    path("", include("provinces.urls")),
    path("tarifler/", include("recipes.urls")),
    path("etkilesim/", include("interactions.urls")),
    path("hesap/", include("accounts.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )