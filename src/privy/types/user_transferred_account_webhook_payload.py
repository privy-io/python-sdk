# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .user import User
from .._models import BaseModel
from .linked_account import LinkedAccount
from .user_reference import UserReference

__all__ = ["UserTransferredAccountWebhookPayload"]


class UserTransferredAccountWebhookPayload(BaseModel):
    """Payload for the user.transferred_account webhook event."""

    account: LinkedAccount
    """A linked account for the user."""

    deleted_user: Literal[True] = FieldInfo(alias="deletedUser")

    from_user: UserReference = FieldInfo(alias="fromUser")
    """A reference to a user by their unique identifier."""

    to_user: User = FieldInfo(alias="toUser")
    """A Privy user object."""

    type: Literal["user.transferred_account"]
    """The type of webhook event."""
