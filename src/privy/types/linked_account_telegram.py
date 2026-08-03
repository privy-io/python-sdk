# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountTelegram"]


class LinkedAccountTelegram(BaseModel):
    """A Telegram account linked to the user."""

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    telegram_user_id: str

    type: Literal["telegram"]

    verified_at: float

    first_name: Optional[str] = None

    last_name: Optional[str] = None

    photo_url: Optional[str] = None

    username: Optional[str] = None
