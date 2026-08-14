# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..transaction_detail import TransactionDetail
from ..blockchain_transaction_status import BlockchainTransactionStatus

__all__ = ["TransactionGetResponse", "Transaction"]


class Transaction(BaseModel):
    caip2: str

    created_at: float

    details: TransactionDetail
    """Details of a wallet transaction, varying by transaction type."""

    privy_transaction_id: Optional[str] = None
    """
    Privy's ID for the transaction, or `null` if the transaction was not broadcasted
    through Privy.
    """

    status: BlockchainTransactionStatus
    """Status of a blockchain transaction submitted by Privy."""

    transaction_hash: Optional[str] = None

    wallet_id: str
    """The wallet whose history this transaction belongs to.

    The sending wallet for outbound transactions, including every transaction Privy
    broadcasted, and the receiving wallet for inbound transfers.
    """

    sponsored: Optional[bool] = None

    user_operation_hash: Optional[str] = None


class TransactionGetResponse(BaseModel):
    next_cursor: Optional[str] = None

    transactions: List[Transaction]
