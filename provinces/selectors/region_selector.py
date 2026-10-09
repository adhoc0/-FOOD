from __future__ import annotations

from django.db.models import QuerySet

from provinces.models import Region


class RegionSelector:
    """Bölge verisini yalnızca okuyan sorgular."""

    @staticmethod
    def get_active_list() -> QuerySet[Region]:
        return Region.objects.filter(is_active=True).order_by("display_order", "name")
