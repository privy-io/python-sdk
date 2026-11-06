# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .tmmf_fund import TmmfFund
from .tmmf_chain import TmmfChain
from .tmmf_provider import TmmfProvider
from .tmmf_order_action_response import TmmfOrderActionResponse

__all__ = ["TmmfPosition"]


class TmmfPosition(BaseModel):
    """A wallet's position in one fund on one chain.

    Fields read from the provider are null when that call fails.
    """

    chain: TmmfChain
    """Chain the fund is held on, e.g. "ethereum_sepolia"."""

    fund: TmmfFund
    """Fund ticker, e.g. "WTGXX". Case-insensitive."""

    nav_date: Optional[str] = None
    """Publication date of the NAV, e.g.

    "2026-09-25", or null without one or when the provider call fails.
    """

    nav_usd: Optional[str] = None
    """Latest published NAV per share in USD, or null when the provider call fails."""

    pending_dividends_usd: Optional[str] = None
    """
    Accrued, undistributed income in USD that is not yet spendable, or null when the
    provider call fails.
    """

    pending_orders: List[TmmfOrderActionResponse]
    """Wallet actions for purchases and redemptions that are still pending."""

    pending_since: Optional[str] = None
    """Start date of the open accrual period, e.g.

    "2026-09-01", or null without one or when the provider call fails.
    """

    provider: TmmfProvider
    """The fund provider."""

    share_value_usd: Optional[str] = None
    """`shares` valued at `nav_usd`, or null when the provider call fails."""

    shares: str
    """Fund shares held on-chain by the wallet."""

    total_position_value_usd: Optional[str] = None
    """
    Estimated share value plus available pending dividends, excluding settlement
    currency and in-transit assets; null without NAV.
    """
