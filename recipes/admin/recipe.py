from django.contrib import admin
from recipes.models import Recipe, RecipeIngredient, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    autocomplete_fields = ['ingredient']

class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'province', 'difficulty', 'is_published', 'created_at')
    list_filter = ('is_published', 'difficulty', 'province')
    search_fields = ('title', 'description', 'province__name')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [RecipeIngredientInline, RecipeImageInline]
    
    fieldsets = (
        ('Genel Bilgiler', {
            'fields': ('title', 'slug', 'description', 'instructions', 'province', 'is_published')
        }),
        ('Detaylar', {
            'fields': ('prep_time_minutes', 'cook_time_minutes', 'serving_size', 'difficulty')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )
