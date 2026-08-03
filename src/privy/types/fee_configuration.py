# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FeeConfiguration"]


class FeeConfiguration(BaseModel):
    """Total fees assessed on a transfer, in BPS"""

    type: Literal["total_fee_bps"]
    """Discriminator: total fee specified in BPS."""

    value: int
    """Total fee in basis points (1 bps = 0.01%)."""
