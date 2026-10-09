from __future__ import annotations

from django.views.generic import TemplateView


class CookiesPageView(TemplateView):
    template_name = "pages/cookies.html"
