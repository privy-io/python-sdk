# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "TransactionGetResponse",
    "Transaction",
    "TransactionDetails",
    "TransactionDetailsUnionMember0",
    "TransactionDetailsUnionMember1",
]


class TransactionDetailsUnionMember0(BaseModel):
    asset: Literal["usdc", "eth", "pol", "sol"]

    chain: Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"]

    display_values: Dict[str, str]

    raw_value: str

    raw_value_decimals: float

    recipient: str

    recipient_privy_user_id: Optional[str] = None

    sender: str

    sender_privy_user_id: Optional[str] = None

    type: Literal["transfer_sent"]


class TransactionDetailsUnionMember1(BaseModel):
    asset: Literal["usdc", "eth", "pol", "sol"]

    chain: Literal["ethereum", "arbitrum", "base", "linea", "optimism", "polygon", "solana", "zksync_era"]

    display_values: Dict[str, str]

    raw_value: str

    raw_value_decimals: float

    recipient: str

    recipient_privy_user_id: Optional[str] = None

    sender: str

    sender_privy_user_id: Optional[str] = None

    type: Literal["transfer_received"]


TransactionDetails: TypeAlias = Union[TransactionDetailsUnionMember0, TransactionDetailsUnionMember1, None]


class Transaction(BaseModel):
    caip2: str

    created_at: float

    details: Optional[TransactionDetails] = None

    privy_transaction_id: str

    status: Literal["broadcasted", "confirmed", "execution_reverted", "failed"]

    transaction_hash: Optional[str] = None

    wallet_id: str


class TransactionGetResponse(BaseModel):
    next_cursor: Optional[str] = None

    transactions: List[Transaction]
