# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .external_fiat_account_swift_category import ExternalFiatAccountSwiftCategory
from .external_fiat_account_swift_purpose_of_funds import ExternalFiatAccountSwiftPurposeOfFunds

__all__ = ["ExternalFiatAccountSwiftDataParam"]


class ExternalFiatAccountSwiftDataParam(TypedDict, total=False):
    """SWIFT bank account data for an external fiat account.

    Pays out over wire. The beneficiary address is required for SWIFT and is supplied as the request's top-level `address`.
    """

    account_number: Required[str]

    bic: Required[str]
    """The BIC/SWIFT code of the beneficiary bank."""

    category: Required[ExternalFiatAccountSwiftCategory]
    """Business relationship between the payer and the SWIFT account owner."""

    purpose_of_funds: Required[List[ExternalFiatAccountSwiftPurposeOfFunds]]

    short_business_description: Required[str]

    type: Required[Literal["swift"]]

    country: str
    """Country the account is held in, as an ISO 3166-1 alpha-3 code."""
