from django.contrib import admin

from recipes.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sort_order",
        "is_active",
    )

    list_display_links = (
        "name",
    )

    list_editable = (
        "sort_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "sort_order",
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            "Genel Bilgiler",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                ),
            },
        ),
        (
            "Görsel",
            {
                "fields": (
                    "image",
                    "icon",
                ),
            },
        ),
        (
            "Durum",
            {
                "fields": (
                    "sort_order",
                    "is_active",
                ),
            },
        ),
        (
            "Kayıt Bilgileri",
            {
                "classes": (
                    "collapse",
                ),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )