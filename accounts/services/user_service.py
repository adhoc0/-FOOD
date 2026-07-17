from __future__ import annotations

from django.contrib.auth import get_user_model
from django.db import transaction

User = get_user_model()


@transaction.atomic
def create_user(
    **validated_data,
):
    """Create a new user."""

    password = validated_data.pop(
        "password",
    )

    user = User(**validated_data)

    user.set_password(
        password,
    )

    user.save()

    return user


@transaction.atomic
def update_user(
    user,
    **validated_data,
):
    """Update an existing user."""

    password = validated_data.pop(
        "password",
        None,
    )

    for field, value in validated_data.items():
        setattr(
            user,
            field,
            value,
        )

    if password:
        user.set_password(
            password,
        )

    user.save()

    return user


@transaction.atomic
def activate_user(
    user,
):
    """Activate user."""

    user.is_active = True

    user.save(
        update_fields=[
            "is_active",
        ],
    )

    return user


@transaction.atomic
def deactivate_user(
    user,
):
    """Deactivate user."""

    user.is_active = False

    user.save(
        update_fields=[
            "is_active",
        ],
    )

    return user
