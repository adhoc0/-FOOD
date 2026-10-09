from __future__ import annotations

from typing import Any

from django.db.models import QuerySet
from django.http import Http404
from django.views.generic import DetailView, ListView

from provinces.models import Province
from provinces.selectors import ProvinceSelector, RegionSelector
from recipes.selectors import RecipeSelector


class ProvinceListView(ListView):
    """Aktif illeri sayfalı olarak gösterir."""

    model = Province
    template_name = "provinces/list.html"
    context_object_name = "provinces"
    paginate_by = 81

    def get_queryset(self) -> QuerySet[Province]:
        region_slug = self.request.GET.get("region", "").strip()
        return ProvinceSelector.get_active_list(region_slug=region_slug)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["regions"] = RegionSelector.get_active_list()
        context["current_region"] = self.request.GET.get("region", "").strip()
        return context


class ProvinceDetailView(DetailView):
    """Tek bir aktif ili gösterir."""

    model = Province
    template_name = "provinces/detail.html"
    context_object_name = "province"
    featured_recipe_limit = 6

    def get_object(self, queryset: QuerySet[Province] | None = None) -> Province:
        province = ProvinceSelector.get_active_by_slug(self.kwargs["slug"])

        if province is None:
            raise Http404("Province not found.")

        return province

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Yalnızca yayındaki tarifler gösterilir; taslak ve pasif tarifler sızmamalıdır.
        context["recipes"] = RecipeSelector.get_by_province(self.object)[
            : self.featured_recipe_limit
        ]
        return context
