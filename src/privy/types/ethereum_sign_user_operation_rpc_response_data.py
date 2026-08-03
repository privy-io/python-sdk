# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EthereumSignUserOperationRpcResponseData"]


class EthereumSignUserOperationRpcResponseData(BaseModel):
    """Data returned by the EVM `eth_signUserOperation` RPC."""

    encoding: Literal["hex"]

    signature: str
