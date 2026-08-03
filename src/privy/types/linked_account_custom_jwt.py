# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountCustomJwt"]


class LinkedAccountCustomJwt(BaseModel):
    """A custom JWT account linked to the user."""

    custom_user_id: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["custom_auth"]

    verified_at: float
