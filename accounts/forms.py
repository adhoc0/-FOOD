from __future__ import annotations

from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

from accounts.services import login_throttle

User = get_user_model()


class ThrottledAuthenticationForm(AuthenticationForm):
    """Başarısız denemeleri kullanıcı adı bazında sınırlayan giriş formu."""

    def clean(self) -> dict[str, Any]:
        username = self.data.get(self.add_prefix("username"), "") or ""

        if username and login_throttle.is_locked(username):
            raise ValidationError(
                "Çok fazla başarısız giriş denemesi yapıldı. "
                "Lütfen 15 dakika sonra tekrar deneyin.",
                code="locked",
            )

        try:
            cleaned_data = super().clean()
        except ValidationError:
            if username:
                login_throttle.register_failure(username)
            raise

        if username:
            login_throttle.reset(username)

        return cleaned_data


class UserRegistrationForm(UserCreationForm):
    """User registration form."""

    class Meta:
        model = User

        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
