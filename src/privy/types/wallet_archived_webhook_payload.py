# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletArchivedWebhookPayload"]


class WalletArchivedWebhookPayload(BaseModel):
    """Payload for the wallet.archived webhook event."""

    archived_at: float
    """Unix timestamp of when the wallet was archived."""

    chain_type: str
    """The chain type of the archived wallet."""

    type: Literal["wallet.archived"]
    """The type of webhook event."""

    wallet_address: str
    """The address of the archived wallet."""

    wallet_id: str
    """The ID of the archived wallet."""
