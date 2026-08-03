# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EthereumSignTypedDataRpcResponseData"]


class EthereumSignTypedDataRpcResponseData(BaseModel):
    """Data returned by the EVM `eth_signTypedData_v4` RPC."""

    encoding: Literal["hex"]

    signature: str
