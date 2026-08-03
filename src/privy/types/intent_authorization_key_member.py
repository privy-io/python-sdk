# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IntentAuthorizationKeyMember"]


class IntentAuthorizationKeyMember(BaseModel):
    """A key member of an intent authorization quorum."""

    public_key: str
    """Public key of the key quorum member"""

    signed_at: Optional[float] = None
    """Unix timestamp when this member signed, or null if not yet signed."""

    type: Literal["key"]
