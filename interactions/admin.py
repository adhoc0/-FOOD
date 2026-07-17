from django.contrib import admin

from .models import Comment, Favorite, Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe", "score", "created_at")
    list_filter = ("score", "created_at")
    search_fields = ("user__username", "recipe__title")
    readonly_fields = ("created_at",)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "recipe__title")
    readonly_fields = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("user__username", "recipe__title", "content")
    list_editable = ("is_approved",)
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} yorum başarıyla onaylandı.")

    approve_comments.short_description = "Seçilen yorumları onayla"
