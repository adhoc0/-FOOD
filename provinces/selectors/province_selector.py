from __future__ import annotations

from provinces.models import Province


class ProvinceSelector:
    """Read-only queries for provinces."""

    @staticmethod
    def get_all():
        return Province.objects.filter(
            is_active=True,
        ).order_by("name")

    @staticmethod
    def get_popular(limit: int = 12):
        return (
            Province.objects.filter(
                is_active=True,
            )
            .order_by("-recipe_count", "name")[:limit]
        )

    @staticmethod
    def get_count() -> int:
        return Province.objects.filter(
            is_active=True,
        ).count()