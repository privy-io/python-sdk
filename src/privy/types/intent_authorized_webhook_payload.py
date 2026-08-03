# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .intent_type import IntentType
from .intent_authorization_key_quorum_member import IntentAuthorizationKeyQuorumMember

__all__ = ["IntentAuthorizedWebhookPayload"]


class IntentAuthorizedWebhookPayload(BaseModel):
    """Payload for the intent.authorized webhook event."""

    authorized_at: float
    """Unix timestamp when the authorization was recorded."""

    created_at: float
    """Unix timestamp when the intent was created."""

    expires_at: float
    """Unix timestamp when the intent expires."""

    intent_id: str
    """The unique ID of the intent."""

    intent_type: IntentType
    """Type of intent."""

    member: IntentAuthorizationKeyQuorumMember
    """A leaf member (user or key) of a nested key quorum in an intent authorization."""

    status: str
    """The current status of the intent."""

    type: Literal["intent.authorized"]
    """The type of webhook event."""

    created_by_display_name: Optional[str] = None
    """Display name of the user who created the intent."""

    created_by_id: Optional[str] = None
    """The ID of the user who created the intent."""
