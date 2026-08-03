# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .authorization_key import AuthorizationKey

__all__ = ["KeyQuorum"]


class KeyQuorum(BaseModel):
    """A key quorum for authorizing wallet operations."""

    id: str

    authorization_keys: List[AuthorizationKey]

    authorization_threshold: Optional[float] = None

    display_name: Optional[str] = None

    user_ids: Optional[List[str]] = None

    key_quorum_ids: Optional[List[str]] = None
    """List of nested key quorum IDs that are members of this key quorum."""
