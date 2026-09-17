# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KYBPubliclyTradedListingParam"]


class KYBPubliclyTradedListingParam(TypedDict, total=False):
    """A public exchange listing for the business."""

    market_identifier_code: Required[str]
    """ISO 10383 market identifier code of the listing venue."""

    stock_number: Required[str]
    """ISIN with dashes removed."""

    ticker: Required[str]
    """Exchange ticker symbol."""
