from django.contrib import admin

from recipes.models import Recipe, RecipeImage, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    autocomplete_fields = ("ingredient",)


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
        "is_featured",
        "is_active",
        "created_at",
    )

    list_filter = (
        "status",
        "difficulty",
        "province",
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "summary",
        "province__name",
        "category__name",
    )

    ordering = (
        "-created_at",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    autocomplete_fields = (
        "province",
        "category",
        "author",
    )

    readonly_fields = (
        "view_count",
        "favorite_count",
        "created_at",
        "updated_at",
    )

    inlines = (
        RecipeIngredientInline,
        RecipeImageInline,
    )

    fieldsets = (
        (
            "Genel Bilgiler",
            {
                "fields": (
                    "title",
                    "slug",
                    "province",
                    "category",
                    "author",
                    "summary",
                    "instructions",
                ),
            },
        ),
        (
            "Hazırlama",
            {
                "fields": (
                    "preparation_time",
                    "cooking_time",
                    "servings",
                    "difficulty",
                ),
            },
        ),
        (
            "Yayın",
            {
                "fields": (
                    "status",
                    "is_featured",
                    "is_active",
                    "published_at",
                ),
            },
        ),
        (
            "SEO",
            {
                "classes": ("collapse",),
                "fields": (
                    "meta_title",
                    "meta_description",
                    "youtube_url",
                    "source_url",
                ),
            },
        ),
        (
            "İstatistikler",
            {
                "classes": ("collapse",),
                "fields": (
                    "view_count",
                    "favorite_count",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )