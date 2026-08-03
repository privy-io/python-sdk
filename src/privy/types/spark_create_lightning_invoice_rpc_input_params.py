# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SparkCreateLightningInvoiceRpcInputParams"]


class SparkCreateLightningInvoiceRpcInputParams(BaseModel):
    """Parameters for the Spark `createLightningInvoice` RPC."""

    amount_sats: float

    description_hash: Optional[str] = None

    expiry_seconds: Optional[float] = None

    include_spark_address: Optional[bool] = None

    memo: Optional[str] = None

    receiver_identity_pubkey: Optional[str] = None
