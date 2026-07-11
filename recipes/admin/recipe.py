from django.contrib import admin

from recipes.models import Recipe, RecipeImage, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "province",
        "category",
        "difficulty",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "difficulty",
        "province",
        "category",
    )

    search_fields = (
        "title",
        "summary",
    )