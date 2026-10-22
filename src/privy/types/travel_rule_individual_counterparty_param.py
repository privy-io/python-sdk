# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .verification_address_param import VerificationAddressParam

__all__ = ["TravelRuleIndividualCounterpartyParam"]


class TravelRuleIndividualCounterpartyParam(TypedDict, total=False):
    """The bank-side party is a person other than the customer."""

    name: Required[str]
    """Full legal name of the person."""

    type: Required[Literal["individual"]]

    address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""
