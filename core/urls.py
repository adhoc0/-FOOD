"""
URL configuration — Türkiye Yöresel Yemekleri

Neden media URL'leri sadece DEBUG modunda ekleniyor?
─────────────────────────────────────────────
Production'da media dosyaları Nginx tarafından servis edilir.
Django'nun development server'ı üzerinden servis etmek:
1. Yavaş (tek thread)
2. Güvensiz (dosya erişim kontrolü yok)

Bu pattern Django'nun resmi dokümantasyonunda önerilen yaklaşımdır.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# ── Admin Panel Özelleştirmesi ──
admin.site.site_header = 'Türkiye Yöresel Yemekleri — Yönetim'
admin.site.site_title = 'Lezzet Haritası Admin'
admin.site.index_title = 'Yönetim Paneli'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('provinces.urls')),
    path('tarifler/', include('recipes.urls')),
    path('etkilesim/', include('interactions.urls')),
    path('hesap/', include('accounts.urls')),
    # Sprint 6'da eklenecek:
    # path('api/', include('api.urls')),
]

# Development'ta media dosyalarını Django serve etsin
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
