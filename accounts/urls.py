from __future__ import annotations

from django.urls import path

from accounts.views import (
    MFASetupView,
    MFAVerifyView,
    UserLoginView,
    UserLogoutView,
    UserPasswordResetCompleteView,
    UserPasswordResetConfirmView,
    UserPasswordResetDoneView,
    UserPasswordResetView,
    UserProfileView,
    UserRegisterView,
)

app_name = "accounts"

urlpatterns = [
    path(
        "login/",
        UserLoginView.as_view(),
        name="login",
    ),
    path(
        "logout/",
        UserLogoutView.as_view(),
        name="logout",
    ),
    path(
        "register/",
        UserRegisterView.as_view(),
        name="register",
    ),
    path(
        "profil/",
        UserProfileView.as_view(),
        name="profile",
    ),
    path(
        "2fa/kurulum/",
        MFASetupView.as_view(),
        name="mfa_setup",
    ),
    path(
        "2fa/dogrula/",
        MFAVerifyView.as_view(),
        name="mfa_verify",
    ),
    path(
        "password-reset/",
        UserPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        UserPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password-reset/complete/",
        UserPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
