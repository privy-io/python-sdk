# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_claim_static_deposit_rpc_input_params import SparkClaimStaticDepositRpcInputParams

__all__ = ["SparkClaimStaticDepositRpcInput"]


class SparkClaimStaticDepositRpcInput(BaseModel):
    """Claims a static deposit into the Spark wallet."""

    method: Literal["claimStaticDeposit"]

    params: SparkClaimStaticDepositRpcInputParams
    """Parameters for the Spark `claimStaticDeposit` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
