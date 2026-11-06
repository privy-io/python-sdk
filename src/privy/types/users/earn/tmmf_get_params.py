# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...wallets.tmmf_provider_param import TmmfProviderParam

__all__ = ["TmmfGetParams"]


class TmmfGetParams(TypedDict, total=False):
    provider: TmmfProviderParam
    """The fund provider."""

    wallet_id: str
    """Only return the registration of this wallet."""

    wallets_cursor: str
    """Cursor returned by the previous page."""

    wallets_limit: int
    """Maximum number of wallet registrations to return."""
