
from __future__ import annotations

from provinces.models import Province


def activate_province(
    provinces: Province,
) -> Province:
    provinces.is_active = True

    provinces.save(
        update_fields=[
            "is_active",
            "updated_at",
        ],
    )

    return provinces


def deactivate_province(
    provinces: Province,
) -> Province:
    provinces.is_active = False

    provinces.save(
        update_fields=[
            "is_active",
            "updated_at",
        ],
    )

    return provinces


def feature_province(
    provinces: Province,
) -> Province:
    provinces.is_featured = True

    provinces.save(
        update_fields=[
            "is_featured",
            "updated_at",
        ],
    )

    return provinces


def unfeature_province(
    provinces: Province,
) -> Province:
    provinces.is_featured = False

    provinces.save(
        update_fields=[
            "is_featured",
            "updated_at",
        ],
    )

    return provinces
