from __future__ import annotations

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import ThrottledAuthenticationForm, UserRegistrationForm
from accounts.selectors import ProfileSelector


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = ThrottledAuthenticationForm


class UserLogoutView(LogoutView):
    pass


class UserPasswordResetView(PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    email_template_name = "accounts/emails/password_reset_email.txt"
    subject_template_name = "accounts/emails/password_reset_subject.txt"
    success_url = reverse_lazy("accounts:password_reset_done")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


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
