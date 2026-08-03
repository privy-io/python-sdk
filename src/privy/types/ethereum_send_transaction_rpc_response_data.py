# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .caip_2 import Caip2
from .._models import BaseModel
from .unsigned_ethereum_transaction import UnsignedEthereumTransaction

__all__ = ["EthereumSendTransactionRpcResponseData"]


class EthereumSendTransactionRpcResponseData(BaseModel):
    """Data returned by the EVM `eth_sendTransaction` RPC."""

    caip2: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    hash: str

    reference_id: Optional[str] = None

    transaction_id: Optional[str] = None

    transaction_request: Optional[UnsignedEthereumTransaction] = None
    """An unsigned Ethereum transaction object.

    Supports standard EVM transaction types (0, 1, 2, 4) and Tempo transactions
    (type 118).
    """

    user_operation_hash: Optional[str] = None
