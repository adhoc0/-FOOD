from __future__ import annotations

from django.urls import path

from accounts.views import (
    UserLoginView,
    UserLogoutView,
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
]
