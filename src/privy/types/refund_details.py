# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RefundDetails"]


class RefundDetails(BaseModel):
    """Relay details for a refunded wallet deposit."""

    original_transaction_hash: str
    """The transaction hash of the transfer that was refunded."""

    provider: Literal["relay"]
    """The provider that handled the refund."""

    wallet_action_id: str
    """The Privy wallet action ID of the transfer that was refunded."""
