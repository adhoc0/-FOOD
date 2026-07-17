from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Kullanıcı yönetimi uygulama konfigürasyonu."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
    verbose_name = "Kullanıcı Yönetimi"
