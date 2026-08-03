# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkTransferRpcInputParams"]


class SparkTransferRpcInputParams(BaseModel):
    """Parameters for the Spark `transfer` RPC."""

    amount_sats: float

    receiver_spark_address: str
