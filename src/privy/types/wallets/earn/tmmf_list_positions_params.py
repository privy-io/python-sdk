# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..tmmf_fund import TmmfFund
from ..tmmf_chain import TmmfChain
from ..tmmf_provider_param import TmmfProviderParam

__all__ = ["TmmfListPositionsParams"]


class TmmfListPositionsParams(TypedDict, total=False):
    chain: TmmfChain
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    cursor: str
    """Cursor returned by the previous page."""

    fund: TmmfFund
    """Fund ticker, e.g. "WTGXX". Case-insensitive."""

    limit: int

    provider: TmmfProviderParam
    """The fund provider."""
