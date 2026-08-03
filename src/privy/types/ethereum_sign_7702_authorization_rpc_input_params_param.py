# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .quantity_param import QuantityParam

__all__ = ["EthereumSign7702AuthorizationRpcInputParamsParam"]


class EthereumSign7702AuthorizationRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the EVM `eth_sign7702Authorization` RPC."""

    chain_id: Required[QuantityParam]
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """

    contract: Required[str]

    executor: Literal["self"]

    nonce: QuantityParam
    """
    A quantity value that can be either a hex string starting with '0x' or a
    non-negative integer.
    """
