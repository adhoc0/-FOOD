from __future__ import annotations

from django.contrib import admin

from provinces.models import Province


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = (
        "plate_code",
        "name",
        "region",
        "is_featured",
        "is_active",
        "created_at",
    )

    list_display_links = ("name",)

    list_editable = (
        "is_featured",
        "is_active",
    )

    list_filter = (
        "region",
        "is_featured",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "plate_code",
        "slug",
        "description",
    )

    autocomplete_fields = ("region",)

    ordering = ("plate_code",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 25

    save_on_top = True

    fieldsets = (
        (
            "Province",
            {
                "fields": (
                    "region",
                    "plate_code",
                    "name",
                    "slug",
                    "description",
                ),
            },
        ),
        (
            "Map",
            {
                "fields": (
                    "latitude",
                    "longitude",
                    "map_x",
                    "map_y",
                ),
            },
        ),
        (
            "Status",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                ),
            },
        ),
        (
            "Metadata",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
