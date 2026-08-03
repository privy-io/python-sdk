# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .intent_authorization_member import IntentAuthorizationMember

__all__ = ["IntentAuthorization"]


class IntentAuthorization(BaseModel):
    """Authorization quorum for an intent"""

    members: List[IntentAuthorizationMember]
    """Members in this authorization quorum"""

    threshold: float
    """Number of signatures required to satisfy this quorum"""

    display_name: Optional[str] = None
    """Display name of the key quorum"""
