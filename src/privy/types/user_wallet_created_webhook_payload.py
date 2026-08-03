# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .user import User
from .._models import BaseModel
from .linked_account_base_wallet import LinkedAccountBaseWallet

__all__ = ["UserWalletCreatedWebhookPayload"]


class UserWalletCreatedWebhookPayload(BaseModel):
    """Payload for the user.wallet_created webhook event."""

    type: Literal["user.wallet_created"]
    """The type of webhook event."""

    user: User
    """A Privy user object."""

    wallet: LinkedAccountBaseWallet
    """Base schema for wallet accounts linked to the user."""
