# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
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

    reference_id: Optional[str] = None

    sponsored: Optional[bool] = None

    user_operation_hash: Optional[str] = None
