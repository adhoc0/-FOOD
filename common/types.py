from __future__ import annotations

from typing import Protocol


class UserLike(Protocol):
    """Protocol representing authenticated and anonymous users."""

    @property
    def is_authenticated(self) -> bool:
        ...
