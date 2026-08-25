# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExternalFiatAccountAddressParam"]


class ExternalFiatAccountAddressParam(TypedDict, total=False):
    """Physical address associated with an external fiat account."""

    city: Required[str]

    country: Required[str]

    street_line_1: Required[str]

    postal_code: str

    state: str

    street_line_2: str
