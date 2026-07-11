from django.views.generic import TemplateView
from .services import HomePageService, SEOService
from provinces.models import Province
from recipes.models import Recipe




class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(HomePageService.get_context())
        context.update(SEOService.homepage())

        return context



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'pages/privacy.html'


class CookiePolicyView(TemplateView):
    template_name = 'pages/cookies.html'


class TermsOfServiceView(TemplateView):
    template_name = 'pages/terms.html'


class KVKKPageView(TemplateView):
    template_name = 'pages/kvkk.html'