# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TransactionConfirmedWebhookPayload"]


class TransactionConfirmedWebhookPayload(BaseModel):
    """Payload for the transaction.confirmed webhook event."""

    caip2: str
    """
    The CAIP-2 chain identifier (e.g., eip155:4217 for Tempo, eip155:1 for Ethereum
    mainnet).
    """

    transaction_hash: str
    """The blockchain transaction hash."""

    transaction_id: str
    """The Privy-assigned ID for this transaction."""

    type: Literal["transaction.confirmed"]
    """The type of webhook event."""

    wallet_id: str
    """The ID of the wallet that initiated the transaction."""

    reference_id: Optional[str] = None
    """
    Developer-provided reference ID for transaction reconciliation, if one was
    provided.
    """
