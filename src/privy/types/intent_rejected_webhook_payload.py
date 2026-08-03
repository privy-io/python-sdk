# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .intent_type import IntentType

__all__ = ["IntentRejectedWebhookPayload"]


class IntentRejectedWebhookPayload(BaseModel):
    """Payload for the intent.rejected webhook event."""

    created_at: float
    """Unix timestamp when the intent was created."""

    expires_at: float
    """Unix timestamp when the intent expires."""

    intent_id: str
    """The unique ID of the intent."""

    intent_type: IntentType
    """Type of intent."""

    rejected_at: float
    """Unix timestamp when the intent was rejected."""

    status: str
    """The current status of the intent."""

    type: Literal["intent.rejected"]
    """The type of webhook event."""

    created_by_display_name: Optional[str] = None
    """Display name of the user who created the intent."""

    created_by_id: Optional[str] = None
    """The ID of the user who created the intent."""
