# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountInstagramOAuth"]


class LinkedAccountInstagramOAuth(BaseModel):
    """An Instagram OAuth account linked to the user."""

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    subject: str

    type: Literal["instagram_oauth"]

    username: Optional[str] = None

    verified_at: float
