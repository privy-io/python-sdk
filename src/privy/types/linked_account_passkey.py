# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LinkedAccountPasskey"]


class LinkedAccountPasskey(BaseModel):
    """A passkey account linked to the user."""

    credential_id: str

    enrolled_in_mfa: bool

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    type: Literal["passkey"]

    verified_at: float

    authenticator_name: Optional[str] = None

    created_with_browser: Optional[str] = None

    created_with_device: Optional[str] = None

    created_with_os: Optional[str] = None

    public_key: Optional[str] = None
