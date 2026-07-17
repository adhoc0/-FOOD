from django.db import models

from provinces.querysets.province_queryset import ProvinceQuerySet


class ProvinceManager(models.Manager.from_queryset(ProvinceQuerySet)):
    """İl sorguları için özel yönetici."""

    use_in_migrations = True

    pass
