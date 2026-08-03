# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .unsigned_standard_ethereum_transaction import UnsignedStandardEthereumTransaction

__all__ = ["TransactionStillPendingWebhookPayload"]


class TransactionStillPendingWebhookPayload(BaseModel):
    """Payload for the transaction.still_pending webhook event."""

    caip2: str
    """
    The CAIP-2 chain identifier (e.g., eip155:4217 for Tempo, eip155:1 for Ethereum
    mainnet).
    """

    transaction_hash: str
    """The blockchain transaction hash."""

    transaction_id: str
    """The Privy-assigned ID for this transaction."""

    transaction_request: UnsignedStandardEthereumTransaction
    """An unsigned standard Ethereum transaction object.

    Supports EVM transaction types 0, 1, 2, and 4.
    """

    type: Literal["transaction.still_pending"]
    """The type of webhook event."""

    wallet_id: str
    """The ID of the wallet that initiated the transaction."""

    reference_id: Optional[str] = None
    """
    Developer-provided reference ID for transaction reconciliation, if one was
    provided.
    """
