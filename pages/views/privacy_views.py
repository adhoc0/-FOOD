from __future__ import annotations

from django.views.generic import TemplateView


class PrivacyPageView(TemplateView):
    template_name = "pages/privacy.html"
