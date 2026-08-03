# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .ethereum_typed_data_input import EthereumTypedDataInput

__all__ = ["EthereumSignTypedDataRpcInputParams"]


class EthereumSignTypedDataRpcInputParams(BaseModel):
    """Parameters for the EVM `eth_signTypedData_v4` RPC."""

    typed_data: EthereumTypedDataInput
    """EIP-712 typed data object."""
