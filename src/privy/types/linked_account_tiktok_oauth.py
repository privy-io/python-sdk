# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountTiktokOAuth"]


class LinkedAccountTiktokOAuth(BaseModel):
    """A TikTok OAuth account linked to the user."""

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    subject: str

    type: Literal["tiktok_oauth"]

    username: Optional[str] = None

    verified_at: float
