from __future__ import annotations

from provinces.models import Province


class ProvinceSelector:
    """İl verisini yalnızca okuyan sorgular."""

    @staticmethod
    def get_active_list(*, region_slug: str = ""):
        queryset = (
            Province.objects.active()
            .with_related()
            .ordered_by_code()
        )

        if region_slug:
            queryset = queryset.filter(region__slug=region_slug)

        return queryset

    @staticmethod
    def get_active_by_slug(slug: str) -> Province | None:
        return (
            Province.objects.active()
            .with_related()
            .by_slug(slug)
            .first()
        )
