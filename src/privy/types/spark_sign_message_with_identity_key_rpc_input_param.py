# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_sign_message_with_identity_key_rpc_input_params_param import (
    SparkSignMessageWithIdentityKeyRpcInputParamsParam,
)

__all__ = ["SparkSignMessageWithIdentityKeyRpcInputParam"]


class SparkSignMessageWithIdentityKeyRpcInputParam(TypedDict, total=False):
    """Signs a message with the Spark identity key."""

    method: Required[Literal["signMessageWithIdentityKey"]]

    params: Required[SparkSignMessageWithIdentityKeyRpcInputParamsParam]
    """Parameters for the Spark `signMessageWithIdentityKey` RPC."""

    network: SparkNetwork
    """The Spark network."""
