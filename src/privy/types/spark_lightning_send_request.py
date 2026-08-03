# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .spark_lightning_fee import SparkLightningFee

__all__ = ["SparkLightningSendRequest"]


class SparkLightningSendRequest(BaseModel):
    """A Spark Lightning send request."""

    id: str

    created_at: str

    encoded_invoice: str

    fee: SparkLightningFee
    """The fee for a Spark Lightning payment."""

    idempotency_key: str

    network: str

    status: str

    typename: str

    updated_at: str

    payment_preimage: Optional[str] = None

    transfer: Optional[object] = None
