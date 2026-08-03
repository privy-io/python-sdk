# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkGetStaticDepositAddressRpcResponseData"]


class SparkGetStaticDepositAddressRpcResponseData(BaseModel):
    """Data returned by the Spark `getStaticDepositAddress` RPC."""

    address: str
