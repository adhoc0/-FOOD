"""
Test factories — User.

factory-boy ile CustomUser test verileri.
"""

import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    """Standart kullanıcı factory."""

    class Meta:
        model = User
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    first_name = factory.Faker("first_name", locale="tr_TR")
    last_name = factory.Faker("last_name", locale="tr_TR")
    password = factory.PostGenerationMethodCall("set_password", "TestPass123!")
    is_active = True


class AdminFactory(UserFactory):
    """Superuser factory."""

    username = factory.Sequence(lambda n: f"admin{n}")
    is_staff = True
    is_superuser = True
