# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountLineOAuth"]


class LinkedAccountLineOAuth(BaseModel):
    """A LINE OAuth account linked to the user."""

    email: Optional[str] = None

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    name: Optional[str] = None

    profile_picture_url: Optional[str] = None

    subject: str

    type: Literal["line_oauth"]

    verified_at: float
