# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .linked_account import LinkedAccount
from .custom_metadata import CustomMetadata
from .linked_mfa_method import LinkedMfaMethod

__all__ = ["User"]


class User(BaseModel):
    """A Privy user object."""

    id: str

    created_at: float
    """Unix timestamp of when the user was created in seconds."""

    has_accepted_terms: bool
    """Indicates if the user has accepted the terms of service."""

    is_guest: bool
    """Indicates if the user is a guest account user."""

    linked_accounts: List[LinkedAccount]

    mfa_methods: List[LinkedMfaMethod]

    custom_metadata: Optional[CustomMetadata] = None
    """Custom metadata associated with the user."""
