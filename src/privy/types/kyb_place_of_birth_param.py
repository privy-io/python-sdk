# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KYBPlaceOfBirthParam"]


class KYBPlaceOfBirthParam(TypedDict, total=False):
    """Place of birth for an associated person."""

    country: Required[str]
    """ISO 3166-1 alpha-3 country code."""

    city: str
    """City of birth."""
