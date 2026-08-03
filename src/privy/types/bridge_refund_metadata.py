# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeRefundMetadata"]


class BridgeRefundMetadata(BaseModel):
    """Bridge metadata for a refund via liquidation address."""

    drain_id: str

    liquidation_address_id: str

    method: Literal["liquidation_address"]

    original_transaction_hash: str
    """The original deposit transaction hash that triggered the failed drain."""

    type: Literal["refund"]
