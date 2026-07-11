from django.contrib import admin

from recipes.models import RecipeImage


@admin.register(RecipeImage)
class RecipeImageAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "sort_order",
        "is_cover",
        "created_at",
    )

    list_filter = (
        "is_cover",
    )

    search_fields = (
        "recipe__title",
        "alt_text",
    )

    ordering = (
        "recipe",
        "sort_order",
    )