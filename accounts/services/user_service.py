from __future__ import annotations

from typing import Any

from django.db import transaction

from accounts.models import CustomUser


@transaction.atomic
def create_user(
    **validated_data: Any,
) -> CustomUser:
    """Create a new user."""

    password = validated_data.pop(
        "password",
    )

    user = CustomUser(**validated_data)

    user.set_password(
        password,
    )

    user.save()

    return user


@transaction.atomic
def update_user(
    user: CustomUser,
    **validated_data: Any,
) -> CustomUser:
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
    user: CustomUser,
) -> CustomUser:
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
    user: CustomUser,
) -> CustomUser:
    """Deactivate user."""

    user.is_active = False

    user.save(
        update_fields=[
            "is_active",
        ],
    )

    return user
