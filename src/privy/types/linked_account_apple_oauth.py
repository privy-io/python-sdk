# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountAppleOAuth"]


class LinkedAccountAppleOAuth(BaseModel):
    """An Apple OAuth account linked to the user."""

    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: Literal["apple_oauth"]

    verified_at: float
