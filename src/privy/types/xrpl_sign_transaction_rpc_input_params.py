# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["XrplSignTransactionRpcInputParams"]


class XrplSignTransactionRpcInputParams(BaseModel):
    """Parameters for the XRPL `xrpl_signTransaction` RPC."""

    encoding: Literal["hex"]

    transaction: str
