# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerificationAddressParam"]


class VerificationAddressParam(TypedDict, total=False):
    """A postal address used in KYC and KYB data submission."""

    city: Required[str]
    """City."""

    country: Required[str]
    """ISO 3166-1 alpha-3 country code."""

    street_line_1: Required[str]
    """Street address line 1."""

    postal_code: str
    """Postal code. Required for countries that use them."""

    street_line_2: str
    """Street address line 2."""

    subdivision: str
    """ISO 3166-2 state or province code. Required for US addresses."""
