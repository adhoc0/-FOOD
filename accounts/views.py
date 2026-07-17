from __future__ import annotations

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView

from accounts.forms import UserRegistrationForm
from accounts.selectors import ProfileSelector


class UserLoginView(LoginView):
    template_name = "accounts/login.html"


class UserLogoutView(LogoutView):
    pass


class UserRegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserRegistrationForm
    success_url = "/"


class UserProfileView(LoginRequiredMixin, TemplateView):
    """Giriş yapan kullanıcının profil özetini gösterir."""

    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = ProfileSelector.get_favorites(self.request.user)
        context["comments"] = ProfileSelector.get_comments(self.request.user)
        return context
