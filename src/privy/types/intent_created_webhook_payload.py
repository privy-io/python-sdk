# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .intent_type import IntentType
from .intent_authorization import IntentAuthorization

__all__ = ["IntentCreatedWebhookPayload"]


class IntentCreatedWebhookPayload(BaseModel):
    """Payload for the intent.created webhook event."""

    created_at: float
    """Unix timestamp when the intent was created."""

    expires_at: float
    """Unix timestamp when the intent expires."""

    intent_id: str
    """The unique ID of the intent."""

    intent_type: IntentType
    """Type of intent."""

    status: str
    """The current status of the intent."""

    type: Literal["intent.created"]
    """The type of webhook event."""

    authorization_details: Optional[List[IntentAuthorization]] = None
    """Key quorums that can authorize this intent."""

    created_by_display_name: Optional[str] = None
    """Display name of the user who created the intent."""

    created_by_id: Optional[str] = None
    """The ID of the user who created the intent."""
