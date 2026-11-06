# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel

__all__ = ["UserCreatedWebhookPayload"]


class UserCreatedWebhookPayload(BaseModel):
    """Payload for the user.created webhook event."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    type: Literal["user.created"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""
