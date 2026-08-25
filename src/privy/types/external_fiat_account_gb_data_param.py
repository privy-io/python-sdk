# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalFiatAccountGBDataParam"]


class ExternalFiatAccountGBDataParam(TypedDict, total=False):
    """UK bank account data for an external fiat account.

    Pays out over Faster Payments.
    """

    account_number: Required[str]
    """The 8-digit UK bank account number."""

    sort_code: Required[str]
    """The 6-digit sort code, without hyphens."""

    type: Required[Literal["gb"]]
