# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..onramp_asset import OnrampAsset
from ..onramp_chain import OnrampChain
from ..fiat_currency import FiatCurrency
from ..onramp_provider import OnrampProvider
from ..fiat_payment_rail import FiatPaymentRail

__all__ = ["OnrampCreateParams", "Destination", "Source"]


class OnrampCreateParams(TypedDict, total=False):
    amount: Required[str]

    destination: Required[Destination]

    provider: Required[OnrampProvider]
    """Valid set of onramp providers"""

    source: Required[Source]


class Destination(TypedDict, total=False):
    chain: Required[OnrampChain]
    """Supported blockchain chains for onramp and offramp."""

    currency: Required[OnrampAsset]
    """Supported crypto assets for onramp and offramp."""

    to_address: Required[str]


class Source(TypedDict, total=False):
    currency: Required[FiatCurrency]
    """Supported fiat currencies."""

    payment_rail: Required[FiatPaymentRail]
    """Supported fiat payment rails."""
