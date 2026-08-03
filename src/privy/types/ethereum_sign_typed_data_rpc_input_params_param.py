# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .ethereum_typed_data_input_param import EthereumTypedDataInputParam

__all__ = ["EthereumSignTypedDataRpcInputParamsParam"]


class EthereumSignTypedDataRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the EVM `eth_signTypedData_v4` RPC."""

    typed_data: Required[EthereumTypedDataInputParam]
    """EIP-712 typed data object."""
