# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SparkLightningReceiveRequest"]


class SparkLightningReceiveRequest(BaseModel):
    """A Spark Lightning receive request."""

    id: str

    created_at: str

    network: str

    status: str

    typename: str

    updated_at: str

    invoice: Optional[object] = None

    payment_preimage: Optional[str] = None

    receiver_identity_public_key: Optional[str] = None

    transfer: Optional[object] = None
