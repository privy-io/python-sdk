# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountFarcaster"]


class LinkedAccountFarcaster(BaseModel):
    """A Farcaster account linked to the user."""

    fid: float

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    owner_address: str

    type: Literal["farcaster"]

    verified_at: float

    bio: Optional[str] = None

    display_name: Optional[str] = None

    homepage_url: Optional[str] = None

    profile_picture: Optional[str] = None

    profile_picture_url: Optional[str] = None

    signer_public_key: Optional[str] = None

    username: Optional[str] = None
