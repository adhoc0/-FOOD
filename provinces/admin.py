from django.contrib import admin
from .models import Province


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('plate_code', 'name', 'region', 'latitude', 'longitude')
    list_filter = ('region',)
    search_fields = ('name', 'plate_code')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('plate_code',)
