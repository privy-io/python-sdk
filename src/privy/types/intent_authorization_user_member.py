# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntentAuthorizationUserMember"]


class IntentAuthorizationUserMember(BaseModel):
    """A user member of an intent authorization quorum."""

    signed_at: Optional[float] = None
    """Unix timestamp when this member signed, or null if not yet signed."""

    type: Literal["user"]

    user_id: str
    """User ID of the key quorum member"""
