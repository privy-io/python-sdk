# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthorizationKey"]


class AuthorizationKey(BaseModel):
    """A public key authorized to sign on a key quorum."""

    display_name: Optional[str] = None

    public_key: str
