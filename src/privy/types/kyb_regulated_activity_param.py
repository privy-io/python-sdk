# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KYBRegulatedActivityParam"]


class KYBRegulatedActivityParam(TypedDict, total=False):
    """Details of the regulated activity a business is licensed to perform."""

    license_number: Required[str]
    """License number issued by the regulator."""

    primary_regulatory_authority_country: Required[str]
    """ISO 3166-1 alpha-3 country code of the primary regulator."""

    primary_regulatory_authority_name: Required[str]
    """Name of the primary regulator."""

    regulated_activities_description: Required[str]
    """Description of the regulated activities performed."""
