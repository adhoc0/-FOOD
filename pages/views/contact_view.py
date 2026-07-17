from __future__ import annotations

from django.views.generic import TemplateView


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"
