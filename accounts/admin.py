from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom User için admin konfigürasyonu.

    Neden UserAdmin'den extend ediyoruz?
    ─────────────────────────────────────────────
    UserAdmin, Django'nun kullanıcı yönetim arayüzünü sağlar:
    - Şifre hash'leme (admin panelinden şifre girildiğinde)
    - Grup ve izin yönetimi
    - Kullanıcı arama ve filtreleme
    - Şifre değiştirme formu

    Eğer düz ModelAdmin kullansaydık, şifre düz metin olarak
    kaydedilirdi — bu kritik bir güvenlik açığı olurdu.

    İleride CustomUser'a yeni alan eklendiğinde, fieldsets ve
    add_fieldsets'i burada güncelleyeceğiz.
    """

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
