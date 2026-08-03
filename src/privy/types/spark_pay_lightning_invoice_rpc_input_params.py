# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SparkPayLightningInvoiceRpcInputParams"]


class SparkPayLightningInvoiceRpcInputParams(BaseModel):
    """Parameters for the Spark `payLightningInvoice` RPC."""

    invoice: str

    max_fee_sats: float

    amount_sats_to_send: Optional[float] = None

    prefer_spark: Optional[bool] = None
