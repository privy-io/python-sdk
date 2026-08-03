# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .ethereum_sign_typed_data_rpc_response_data import EthereumSignTypedDataRpcResponseData

__all__ = ["EthereumSignTypedDataRpcResponse"]


class EthereumSignTypedDataRpcResponse(BaseModel):
    """Response to the EVM `eth_signTypedData_v4` RPC."""

    data: EthereumSignTypedDataRpcResponseData
    """Data returned by the EVM `eth_signTypedData_v4` RPC."""

    method: Literal["eth_signTypedData_v4"]
