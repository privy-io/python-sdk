# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .intent_authorization_key_quorum_member import IntentAuthorizationKeyQuorumMember

__all__ = ["IntentAuthorizationKeyQuorum"]


class IntentAuthorizationKeyQuorum(BaseModel):
    """A nested key quorum member of an intent authorization quorum."""

    key_quorum_id: str
    """ID of the child key quorum member"""

    members: List[IntentAuthorizationKeyQuorumMember]
    """Members of this child quorum"""

    threshold: float
    """Number of signatures required from this child quorum"""

    threshold_met: bool
    """Whether this child key quorum has met its signature threshold"""

    type: Literal["key_quorum"]

    display_name: Optional[str] = None
    """Display name for the child key quorum (if any)"""
