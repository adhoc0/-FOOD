from __future__ import annotations

from django.db import transaction

from provinces.models import Region


@transaction.atomic
def create_region(
    **validated_data,
) -> Region:
    """Create a new region."""

    return Region.objects.create(
        **validated_data,
    )


@transaction.atomic
def update_region(
    region: Region,
    **validated_data,
) -> Region:
    """Update an existing region."""

    for field, value in validated_data.items():
        setattr(
            region,
            field,
            value,
        )

    region.save()

    return region


@transaction.atomic
def activate_region(
    region: Region,
) -> Region:
    """Activate region."""

    region.is_active = True

    region.save(
        update_fields=[
            "is_active",
            "updated_at",
        ],
    )

    return region


@transaction.atomic
def deactivate_region(
    region: Region,
) -> Region:
    """Deactivate region."""

    region.is_active = False

    region.save(
        update_fields=[
            "is_active",
            "updated_at",
        ],
    )

    return region
