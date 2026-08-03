# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel

__all__ = ["UserCreatedWebhookPayload"]


class UserCreatedWebhookPayload(BaseModel):
    """Payload for the user.created webhook event."""

    type: Literal["user.created"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""
