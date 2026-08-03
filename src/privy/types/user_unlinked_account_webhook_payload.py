# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .linked_account import LinkedAccount

__all__ = ["UserUnlinkedAccountWebhookPayload"]


class UserUnlinkedAccountWebhookPayload(BaseModel):
    """Payload for the user.unlinked_account webhook event."""

    account: LinkedAccount
    """A linked account for the user."""

    type: Literal["user.unlinked_account"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""
