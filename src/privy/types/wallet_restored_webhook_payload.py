# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletRestoredWebhookPayload"]


class WalletRestoredWebhookPayload(BaseModel):
    """Payload for the wallet.restored webhook event."""

    chain_type: str
    """The chain type of the restored wallet."""

    type: Literal["wallet.restored"]
    """The type of webhook event."""

    wallet_address: str
    """The address of the restored wallet."""

    wallet_id: str
    """The ID of the restored wallet."""
