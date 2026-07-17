from __future__ import annotations

from django.contrib import admin

from recipes.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
        "slug",
    )

    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
    )

    ordering = ("name",)

    list_per_page = 25

    save_on_top = True

    fieldsets = (
        (
            "Category",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                ),
            },
        ),
        (
            "Display",
            {
                "fields": (
                    "image",
                    "icon",
                    "is_active",
                ),
            },
        ),
        (
            "Dates",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
