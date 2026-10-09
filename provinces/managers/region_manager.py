from django.db import models


class RegionManager(models.Manager):
    """Bölge kayıtları için varsayılan yönetici."""

    use_in_migrations = True

    pass
