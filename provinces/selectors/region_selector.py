from __future__ import annotations

from provinces.models import Region


class RegionSelector:
    """Bölge verisini yalnızca okuyan sorgular."""

    @staticmethod
    def get_active_list():
        return Region.objects.filter(is_active=True).order_by("display_order", "name")
