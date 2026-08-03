# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_get_static_deposit_address_rpc_response_data import SparkGetStaticDepositAddressRpcResponseData

__all__ = ["SparkGetStaticDepositAddressRpcResponse"]


class SparkGetStaticDepositAddressRpcResponse(BaseModel):
    """Response to the Spark `getStaticDepositAddress` RPC."""

    method: Literal["getStaticDepositAddress"]

    data: Optional[SparkGetStaticDepositAddressRpcResponseData] = None
    """Data returned by the Spark `getStaticDepositAddress` RPC."""
