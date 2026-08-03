# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_personal_sign_rpc_response_data import EthereumPersonalSignRpcResponseData

__all__ = ["EthereumPersonalSignRpcResponse"]


class EthereumPersonalSignRpcResponse(BaseModel):
    """Response to the EVM `personal_sign` RPC."""

    data: EthereumPersonalSignRpcResponseData
    """Data returned by the EVM `personal_sign` RPC."""

    method: Literal["personal_sign"]
