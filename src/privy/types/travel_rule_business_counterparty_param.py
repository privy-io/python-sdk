# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .verification_address_param import VerificationAddressParam

__all__ = ["TravelRuleBusinessCounterpartyParam"]


class TravelRuleBusinessCounterpartyParam(TypedDict, total=False):
    """The bank-side party is a business other than the customer."""

    legal_entity_identifier: Required[str]
    """
    An official business identifier, such as an LEI, VAT number or company
    registration number.
    """

    name: Required[str]
    """Legal name of the business."""

    type: Required[Literal["business"]]

    address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""
