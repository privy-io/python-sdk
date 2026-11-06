# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletRecoveredWebhookPayload"]


class WalletRecoveredWebhookPayload(BaseModel):
    """Payload for the wallet.recovered webhook event."""

    event_id: str
    """
    The ID of this event, stable across repeat deliveries so clients can deduplicate
    on it.
    """

    type: Literal["wallet.recovered"]
    """The type of webhook event."""

    user_id: str
    """The ID of the user."""

    wallet_address: str
    """The address of the wallet."""

    wallet_id: str
    """The ID of the wallet."""
