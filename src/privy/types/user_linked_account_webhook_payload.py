# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .linked_account import LinkedAccount

__all__ = ["UserLinkedAccountWebhookPayload"]


class UserLinkedAccountWebhookPayload(BaseModel):
    """Payload for the user.linked_account webhook event."""

    account: LinkedAccount
    """A linked account for the user."""

    type: Literal["user.linked_account"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""
