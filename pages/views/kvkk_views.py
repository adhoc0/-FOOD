from __future__ import annotations

from django.views.generic import TemplateView


class KVKKPageView(TemplateView):
    template_name = "pages/kvkk.html"
