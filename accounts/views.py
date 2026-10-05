from __future__ import annotations

from typing import Any, cast

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseBase
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.generic import CreateView, FormView, TemplateView

from accounts.forms import OTPCodeForm, ThrottledAuthenticationForm, UserRegistrationForm
from accounts.models import CustomUser
from accounts.selectors import ProfileSelector
from accounts.services import mfa_service


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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user = cast(CustomUser, self.request.user)
        context["favorites"] = ProfileSelector.get_favorites(user)
        context["comments"] = ProfileSelector.get_comments(user)
        return context


class _MFAViewMixin(LoginRequiredMixin, FormView):
    form_class = OTPCodeForm

    @property
    def user_obj(self) -> CustomUser:
        return cast(CustomUser, self.request.user)

    def get_success_url(self) -> str:
        target = self.request.GET.get("next", "")
        if target and url_has_allowed_host_and_scheme(
            target, allowed_hosts={self.request.get_host()}, require_https=self.request.is_secure()
        ):
            return target
        return reverse("accounts:profile")

    def form_valid(self, form: OTPCodeForm) -> HttpResponse:
        mfa_service.mark_verified(self.request)
        return redirect(self.get_success_url())

    def _reject(self, form: OTPCodeForm) -> HttpResponse:
        if mfa_service.is_locked(self.user_obj):
            form.add_error(None, "Çok fazla hatalı deneme. Lütfen 15 dakika sonra tekrar deneyin.")
        else:
            form.add_error("code", "Kod geçersiz veya süresi dolmuş.")
        return self.form_invalid(form)


class MFAVerifyView(_MFAViewMixin):
    """Giriş sonrası 2FA kodunu doğrular."""

    template_name = "accounts/mfa_verify.html"

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseBase:
        if request.user.is_authenticated and not mfa_service.has_confirmed_device(
            cast(CustomUser, request.user)
        ):
            return redirect(f"{reverse('accounts:mfa_setup')}?{request.GET.urlencode()}")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: OTPCodeForm) -> HttpResponse:
        if not mfa_service.verify_code(self.user_obj, form.cleaned_data["code"]):
            return self._reject(form)
        return super().form_valid(form)


class MFASetupView(_MFAViewMixin):
    """Authenticator uygulamasını bağlar (ilk kurulum)."""

    template_name = "accounts/mfa_setup.html"

    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseBase:
        if request.user.is_authenticated and mfa_service.has_confirmed_device(
            cast(CustomUser, request.user)
        ):
            messages.info(request, "İki adımlı doğrulama zaten etkin.")
            return redirect(f"{reverse('accounts:mfa_verify')}?{request.GET.urlencode()}")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        device = mfa_service.get_or_create_pending_device(self.user_obj)
        context["secret"] = device.secret
        context["otpauth_uri"] = mfa_service.provisioning_uri(device, self.user_obj)
        return context

    def form_valid(self, form: OTPCodeForm) -> HttpResponse:
        if not mfa_service.verify_code(self.user_obj, form.cleaned_data["code"], confirm=True):
            return self._reject(form)
        messages.success(self.request, "İki adımlı doğrulama etkinleştirildi.")
        return super().form_valid(form)
