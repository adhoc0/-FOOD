from __future__ import annotations

from django.contrib import admin

from provinces.models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = (
        "display_order",
        "name",
        "slug",
        "map_color",
        "is_active",
        "created_at",
    )

    list_display_links = ("name",)

    list_editable = (
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
        "description",
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

    list_per_page = 25

    save_on_top = True

    fieldsets = (
        (
            "Region",
            {
                "fields": (
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
                    "map_color",
                    "display_order",
                ),
            },
        ),
        (
            "Status",
            {
                "fields": ("is_active",),
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
