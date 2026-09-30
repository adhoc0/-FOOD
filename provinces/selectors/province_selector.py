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
    def get_map_entries() -> list[dict[str, str | int]]:
        """Etkileşimli harita için aktif illerin plaka, ad ve adres bilgisi."""
        return [
            {
                "plate_code": province.plate_code,
                "name": province.name,
                "url": province.get_absolute_url(),
            }
            for province in Province.objects.active().ordered_by_code()
        ]

    @staticmethod
    def get_active_by_slug(slug: str) -> Province | None:
        return (
            Province.objects.active()
            .with_related()
            .by_slug(slug)
            .first()
        )
