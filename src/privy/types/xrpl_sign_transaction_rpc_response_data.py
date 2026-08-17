# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["XrplSignTransactionRpcResponseData"]


class XrplSignTransactionRpcResponseData(BaseModel):
    """Data returned by the XRPL `xrpl_signTransaction` RPC."""

    encoding: Literal["hex"]

    signed_transaction: str

    txn_signature: str
