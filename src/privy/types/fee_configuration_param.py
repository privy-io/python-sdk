# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeeConfigurationParam"]


class FeeConfigurationParam(TypedDict, total=False):
    """Total fees assessed on a transfer, in BPS"""

    type: Required[Literal["total_fee_bps"]]
    """Discriminator: total fee specified in BPS."""

    value: Required[int]
    """Total fee in basis points (1 bps = 0.01%)."""
