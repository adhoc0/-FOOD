from __future__ import annotations

from django.views.generic import TemplateView


class TermsPageView(TemplateView):
    """Kullanım şartları sayfası."""

    template_name = "pages/terms.html"
