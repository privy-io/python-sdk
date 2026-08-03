# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .unsigned_ethereum_transaction_param import UnsignedEthereumTransactionParam

__all__ = ["EthereumSignTransactionRpcInputParamsParam"]


class EthereumSignTransactionRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the EVM `eth_signTransaction` RPC."""

    transaction: Required[UnsignedEthereumTransactionParam]
    """An unsigned Ethereum transaction object.

    Supports standard EVM transaction types (0, 1, 2, 4) and Tempo transactions
    (type 118).
    """
