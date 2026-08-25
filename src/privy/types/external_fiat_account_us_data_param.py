# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalFiatAccountUsDataParam"]


class ExternalFiatAccountUsDataParam(TypedDict, total=False):
    """US bank account data for an external fiat account."""

    account_number: Required[str]

    routing_number: Required[str]

    type: Required[Literal["us"]]

    checking_or_savings: str
