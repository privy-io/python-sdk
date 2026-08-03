# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_sign_message_with_identity_key_rpc_input_params import SparkSignMessageWithIdentityKeyRpcInputParams

__all__ = ["SparkSignMessageWithIdentityKeyRpcInput"]


class SparkSignMessageWithIdentityKeyRpcInput(BaseModel):
    """Signs a message with the Spark identity key."""

    method: Literal["signMessageWithIdentityKey"]

    params: SparkSignMessageWithIdentityKeyRpcInputParams
    """Parameters for the Spark `signMessageWithIdentityKey` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
