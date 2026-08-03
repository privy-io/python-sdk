# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BlockInfo"]


class BlockInfo(BaseModel):
    """Block metadata for a wallet transfer event."""

    number: float
    """The block number."""

    timestamp: float
    """The block timestamp."""
