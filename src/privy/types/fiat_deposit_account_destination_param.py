# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FiatDepositAccountDestinationParam"]


class FiatDepositAccountDestinationParam(TypedDict, total=False):
    """The destination crypto asset and chain for a fiat deposit account."""

    asset: Required[str]
    """Destination crypto asset (e.g. "usdc")."""

    chain: Required[str]
    """Destination chain (e.g. "base", "tempo")."""
