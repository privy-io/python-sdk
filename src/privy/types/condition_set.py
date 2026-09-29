# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .key_quorum_id import KeyQuorumID

__all__ = ["ConditionSet"]


class ConditionSet(BaseModel):
    """A condition set for grouping related condition values."""

    id: str
    """Unique ID of the created condition set.

    This will be the primary identifier when using the condition set in the future.
    """

    created_at: float
    """Unix timestamp of when the condition set was created in milliseconds."""

    name: str
    """Name of the condition set."""

    owner_id: Optional[KeyQuorumID] = None
    """A unique identifier for a key quorum."""
