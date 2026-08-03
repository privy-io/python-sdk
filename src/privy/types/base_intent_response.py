# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .intent_status import IntentStatus
from .intent_authorization import IntentAuthorization

__all__ = ["BaseIntentResponse"]


class BaseIntentResponse(BaseModel):
    """Common fields shared by all intent response types."""

    authorization_details: List[IntentAuthorization]
    """
    Detailed authorization information including key quorum members, thresholds, and
    signature status
    """

    created_at: float
    """Unix timestamp when the intent was created"""

    created_by_display_name: str
    """Display name of the user who created the intent"""

    custom_expiry: bool
    """Whether this intent has a custom expiry time set by the client.

    If false, the intent expires after a default duration.
    """

    expires_at: float
    """Unix timestamp when the intent expires"""

    intent_id: str
    """Unique ID for the intent"""

    resource_id: str
    """ID of the resource being modified (wallet_id, policy_id, etc)"""

    status: IntentStatus
    """Current status of an intent."""

    created_by_id: Optional[str] = None
    """ID of the user who created the intent.

    If undefined, the intent was created using the app secret
    """

    dismissal_reason: Optional[str] = None
    """Human-readable reason for dismissal, present when status is 'dismissed'"""

    dismissed_at: Optional[float] = None
    """
    Unix timestamp when the intent was dismissed, present when status is 'dismissed'
    """

    rejected_at: Optional[float] = None
    """Unix timestamp when the intent was rejected, present when status is 'rejected'"""
