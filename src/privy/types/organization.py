# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .key_quorum_id import KeyQuorumID

__all__ = ["Organization"]


class Organization(BaseModel):
    """A Privy organization object."""

    id: str
    """Unique organization identifier"""

    created_at: float
    """Unix timestamp when the organization was created"""

    default_key_quorum_id: KeyQuorumID
    """A unique identifier for a key quorum."""

    display_name: str
    """Organization display name"""

    updated_at: float
    """Unix timestamp when the organization was last updated"""
