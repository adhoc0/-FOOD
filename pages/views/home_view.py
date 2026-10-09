from __future__ import annotations

from typing import Any

from django.views.generic import TemplateView

from pages.services import HomePageService


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(HomePageService.get_context())
        return context
