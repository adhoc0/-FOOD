from __future__ import annotations

from django.contrib import admin

from recipes.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_filter = ("is_active",)

    search_fields = (
        "name",
        "slug",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("name",)

    list_per_page = 25
