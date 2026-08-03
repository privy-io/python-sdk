# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WalletGetParams"]


class WalletGetParams(TypedDict, total=False):
    include_archived: bool
    """Include archived wallets in lookup. Defaults to false."""
