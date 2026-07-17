from __future__ import annotations

from django.contrib import admin

from recipes.models import Recipe, RecipeImage, RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1
    fields = (
        "image",
        "alt_text",
        "is_cover",
        "sort_order",
    )
    ordering = ("sort_order",)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    autocomplete_fields = ("ingredient",)
    fields = (
        "ingredient",
        "quantity",
        "unit",
        "sort_order",
    )
    ordering = ("sort_order",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "province",
        "category",
        "author",
        "status",
        "is_featured",
        "is_active",
        "view_count",
        "favorite_count",
        "published_at",
    )

    list_display_links = ("title",)

    list_editable = (
        "status",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "status",
        "province",
        "category",
        "difficulty",
        "is_featured",
        "is_active",
        "created_at",
        "published_at",
    )

    search_fields = (
        "title",
        "slug",
        "summary",
        "author__username",
        "province__name",
        "category__name",
    )

    ordering = (
        "-published_at",
        "-created_at",
    )

    readonly_fields = (
        "slug",
        "view_count",
        "favorite_count",
        "created_at",
        "updated_at",
        "published_at",
    )

    autocomplete_fields = (
        "province",
        "category",
        "author",
    )

    list_select_related = (
        "province",
        "category",
        "author",
    )

    inlines = [
        RecipeIngredientInline,
        RecipeImageInline,
    ]

    prepopulated_fields = {
        "slug": ("title",),
    }

    list_per_page = 25

    save_on_top = True

    date_hierarchy = "published_at"

    actions = (
        "mark_active",
        "mark_inactive",
        "mark_featured",
        "unmark_featured",
    )

    fieldsets = (
        (
            "Recipe",
            {
                "fields": (
                    "title",
                    "slug",
                    "province",
                    "category",
                    "author",
                ),
            },
        ),
        (
            "Content",
            {
                "fields": (
                    "summary",
                    "instructions",
                ),
            },
        ),
        (
            "Recipe Information",
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
            "Status",
            {
                "fields": (
                    "status",
                    "is_active",
                    "is_featured",
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
                ),
            },
        ),
        (
            "Media",
            {
                "classes": ("collapse",),
                "fields": (
                    "youtube_url",
                    "source_url",
                ),
            },
        ),
        (
            "Statistics",
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

    @admin.action(description="Seçilen tarifleri aktif yap")
    def mark_active(self, request, queryset):
        queryset.update(
            is_active=True,
        )

    @admin.action(description="Seçilen tarifleri pasif yap")
    def mark_inactive(self, request, queryset):
        queryset.update(
            is_active=False,
        )

    @admin.action(description="Seçilen tarifleri öne çıkar")
    def mark_featured(self, request, queryset):
        queryset.update(
            is_featured=True,
        )

    @admin.action(description="Seçilen tarifleri öne çıkarma")
    def unmark_featured(self, request, queryset):
        queryset.update(
            is_featured=False,
        )
