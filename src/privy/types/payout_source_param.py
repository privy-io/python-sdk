# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PayoutSourceParam"]


class PayoutSourceParam(TypedDict, total=False):
    """The source crypto asset, chain, and amount for a payout."""

    amount: Required[str]
    """Amount to offramp, in the asset's standard units (e.g. "100.00")."""

    asset: Required[str]
    """Source crypto asset (e.g. "usdc")."""

    chain: Required[str]
    """Source chain (e.g. "base")."""
