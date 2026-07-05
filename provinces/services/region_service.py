from django.db import transaction

from provinces.models import Region


@transaction.atomic
def create_region(**data):
    """
    Yeni bölge oluşturur.
    """
    return Region.objects.create(**data)


@transaction.atomic
def update_region(region: Region, **data):
    """
    Bölgeyi günceller.
    """
    for field, value in data.items():
        setattr(region, field, value)

    region.save()

    return region


@transaction.atomic
def activate_region(region: Region):
    """
    Bölgeyi aktif eder.
    """
    region.is_active = True
    region.save(update_fields=["is_active"])


@transaction.atomic
def deactivate_region(region: Region):
    """
    Bölgeyi pasif eder.
    """
    region.is_active = False
    region.save(update_fields=["is_active"])