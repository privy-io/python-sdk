# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountAuthorizationKey"]


class LinkedAccountAuthorizationKey(BaseModel):
    """An authorization key linked to the user."""

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    public_key: str

    type: Literal["authorization_key"]

    verified_at: float
