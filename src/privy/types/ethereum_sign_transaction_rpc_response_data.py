# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EthereumSignTransactionRpcResponseData"]


class EthereumSignTransactionRpcResponseData(BaseModel):
    """Data returned by the EVM `eth_signTransaction` RPC."""

    encoding: Literal["rlp"]

    signed_transaction: str
