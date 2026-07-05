from django.contrib import admin

from provinces.models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display_links = (
    "name",
)
    list_display = (
        "display_order",
        "name",
        "slug",
        "map_color",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
    )

    ordering = (
        "display_order",
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    fieldsets = (
        (
            "Bölge Bilgileri",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                ),
            },
        ),
        (
            "Harita",
            {
                "fields": (
                    "map_color",
                    "display_order",
                ),
            },
        ),
        (
            "Durum",
            {
                "fields": (
                    "is_active",
                ),
            },
        ),
        (
            "Kayıt Bilgileri",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),
    )