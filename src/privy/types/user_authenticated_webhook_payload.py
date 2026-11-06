# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .linked_account import LinkedAccount

__all__ = ["UserAuthenticatedWebhookPayload"]


class UserAuthenticatedWebhookPayload(BaseModel):
    """Payload for the user.authenticated webhook event."""

    account: LinkedAccount
    """A linked account for the user."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    type: Literal["user.authenticated"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""
