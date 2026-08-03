# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .unsigned_ethereum_transaction import UnsignedEthereumTransaction

__all__ = ["EthereumSignTransactionRpcInputParams"]


class EthereumSignTransactionRpcInputParams(BaseModel):
    """Parameters for the EVM `eth_signTransaction` RPC."""

    transaction: UnsignedEthereumTransaction
    """An unsigned Ethereum transaction object.

    Supports standard EVM transaction types (0, 1, 2, 4) and Tempo transactions
    (type 118).
    """
