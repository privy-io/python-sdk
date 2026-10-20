# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .currency_amount import CurrencyAmount
from .blockchain_transaction_status import BlockchainTransactionStatus

__all__ = ["Transaction"]


class Transaction(BaseModel):
    """A transaction from a Privy wallet."""

    id: str

    caip2: str

    created_at: float

    status: BlockchainTransactionStatus
    """Status of a blockchain transaction submitted by Privy."""

    transaction_hash: Optional[str] = None

    wallet_id: str

    gas_credits_charged: Optional[CurrencyAmount] = None
    """A monetary value with its currency denomination."""

    reference_id: Optional[str] = None
    """Developer-provided reference ID, if one was included in the request."""

    sponsored: Optional[bool] = None

    user_operation_hash: Optional[str] = None
