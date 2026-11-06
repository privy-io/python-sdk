# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel

__all__ = ["UserDeletedWebhookPayload"]


class UserDeletedWebhookPayload(BaseModel):
    """Payload for the user.deleted webhook event."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    type: Literal["user.deleted"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""
