# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .kyb_business_type import KYBBusinessType
from .kyb_account_purpose import KYBAccountPurpose
from .kyb_source_of_funds import KYBSourceOfFunds
from .kyb_high_risk_activity import KYBHighRiskActivity
from .verification_address_param import VerificationAddressParam
from .kyb_associated_person_param import KYBAssociatedPersonParam
from .kyb_business_document_param import KYBBusinessDocumentParam
from .verification_document_param import VerificationDocumentParam
from .kyb_estimated_annual_revenue import KYBEstimatedAnnualRevenue
from .kyb_regulated_activity_param import KYBRegulatedActivityParam
from .kyb_publicly_traded_listing_param import KYBPubliclyTradedListingParam

__all__ = ["KYBSubmitDataParam"]


class KYBSubmitDataParam(TypedDict, total=False):
    """KYB verification data for headless submission.

    Fields are individually optional because the provider accepts partial submissions and grants endorsements once enough data has arrived; a partial submission can be completed by calling the endpoint again.
    """

    account_purpose: KYBAccountPurpose
    """Primary purpose the business will use the account for.

    Passthrough to the provider. See the
    [Bridge customer API reference](https://apidocs.bridge.xyz/platform/customers/customers/api)
    for accepted values.
    """

    account_purpose_other: str
    """Free-text purpose. Required when account_purpose is "other"."""

    acting_as_intermediary: bool
    """Whether the business moves funds on behalf of third parties."""

    associated_persons: Iterable[KYBAssociatedPersonParam]
    """Beneficial owners, control persons, and signers."""

    business_description: str
    """Short summary of what the business does."""

    business_industry: SequenceNotStr[str]
    """2022 NAICS codes describing the industries the business operates in."""

    business_legal_name: str
    """Registered legal name as filed with government authorities."""

    business_trade_name: str
    """Public trading name (DBA), if different from the legal name."""

    business_type: KYBBusinessType
    """Legal structure of the business.

    Passthrough to the provider. See the
    [Bridge customer API reference](https://apidocs.bridge.xyz/platform/customers/customers/api)
    for accepted values.
    """

    compliance_screening_explanation: str
    """Description of the AML and sanctions screening controls in place."""

    conducts_money_services: bool
    """Whether the business conducts money services."""

    conducts_money_services_description: str
    """Description of the money services conducted."""

    conducts_money_services_using_bridge: bool
    """Whether money services are conducted through the provider.

    Requires a flow_of_funds document when true.
    """

    documents: Iterable[KYBBusinessDocumentParam]
    """Supporting documents for verification."""

    email: str
    """Primary business email address."""

    estimated_annual_revenue_usd: KYBEstimatedAnnualRevenue
    """Estimated annual revenue of the business, in USD buckets.

    Passthrough to the provider. See the
    [Bridge customer API reference](https://apidocs.bridge.xyz/platform/customers/customers/api)
    for accepted values.
    """

    expected_monthly_payments_usd: int
    """Expected monthly payment volume in USD. Required for high-risk businesses."""

    has_foreign_tax_registration: bool
    """Whether the business is tax-registered outside its country of incorporation."""

    has_material_intermediary_ownership: bool
    """Whether an intermediate entity owner holds 25% or more of the business."""

    high_risk_activities: SequenceNotStr[KYBHighRiskActivity]
    """High-risk activities the business engages in."""

    high_risk_activities_explanation: str
    """Explanation of the high-risk activities.

    Required unless the only value is "none_of_the_above".
    """

    identifying_information: Iterable[VerificationDocumentParam]
    """Business tax and registration identifiers."""

    incorporation_date: str
    """Date of incorporation in YYYY-MM-DD format."""

    is_dao: bool
    """Whether the business is a decentralized autonomous organization."""

    operates_in_prohibited_countries: bool
    """Whether the business operates in prohibited jurisdictions."""

    other_websites: SequenceNotStr[str]
    """Additional websites and social handles."""

    ownership_threshold: int
    """Ownership percentage at which a person is treated as a beneficial owner."""

    phone: str
    """Business phone number in E.164 format."""

    physical_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    primary_website: str
    """Primary website.

    If omitted, a proof_of_nature_of_business document is required.
    """

    publicly_traded_listings: Iterable[KYBPubliclyTradedListingParam]
    """Public exchange listings for the business."""

    registered_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    regulated_activity: KYBRegulatedActivityParam
    """Details of the regulated activity a business is licensed to perform."""

    source_of_funds: KYBSourceOfFunds
    """Primary source of the funds the business will transact with.

    Passthrough to the provider. See the
    [Bridge customer API reference](https://apidocs.bridge.xyz/platform/customers/customers/api)
    for accepted values.
    """

    source_of_funds_description: str
    """Free-text detail on the source of funds. Required for high-risk businesses."""

    transliterated_business_legal_name: str
    """Latin-1 transliteration of the legal name. Required for non-Latin-1 names."""

    transliterated_business_trade_name: str
    """Latin-1 transliteration of the trade name. Required for non-Latin-1 names."""

    transliterated_physical_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    transliterated_registered_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""
