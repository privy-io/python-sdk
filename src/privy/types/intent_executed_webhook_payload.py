# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .intent_type import IntentType
from .base_action_result import BaseActionResult

__all__ = ["IntentExecutedWebhookPayload"]


class IntentExecutedWebhookPayload(BaseModel):
    """Payload for the intent.executed webhook event."""

    action_result: BaseActionResult
    """Result of the successful intent execution."""

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

    type: Literal["intent.executed"]
    """The type of webhook event."""

    created_by_display_name: Optional[str] = None
    """Display name of the user who created the intent."""

    created_by_id: Optional[str] = None
    """The ID of the user who created the intent."""
