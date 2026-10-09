# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .kyx_screen_param import KyxScreenParam
from .kyb_place_of_birth_param import KYBPlaceOfBirthParam
from .verification_address_param import VerificationAddressParam
from .verification_document_param import VerificationDocumentParam
from .kyb_individual_document_param import KYBIndividualDocumentParam

__all__ = ["KYBAssociatedPersonParam"]


class KYBAssociatedPersonParam(TypedDict, total=False):
    """A beneficial owner, control person, or signer associated with the business.

    At least one of has_ownership, has_control, or is_signer must be true, and the business must have at least one control person and one signer.
    """

    date_of_birth: Required[str]
    """Date of birth in YYYY-MM-DD format. Must be 18 years or older."""

    email: Required[str]
    """Email address."""

    first_name: Required[str]
    """Legal first name."""

    has_control: Required[bool]
    """Whether this person is a control person."""

    has_ownership: Required[bool]
    """Whether this person owns 25% or more of the business."""

    identifying_information: Required[Iterable[VerificationDocumentParam]]
    """Identifying documents for this person."""

    is_signer: Required[bool]
    """Whether this person is a signer for the business."""

    last_name: Required[str]
    """Legal last name."""

    residential_address: Required[VerificationAddressParam]
    """A postal address used in KYC and KYB data submission."""

    attested_ownership_structure_at: Annotated[
        Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")
    ]
    """
    When this person (a control person) attested to having verified the business
    ownership structure (ISO 8601).
    """

    documents: Iterable[KYBIndividualDocumentParam]
    """Supporting documents for this person, such as proof of address."""

    is_director: bool
    """Whether this person is a director."""

    kyc_screen: KyxScreenParam
    """
    Result of a KYC/AML or OFAC screen you performed and are relying on the provider
    to accept, honoured only for developers enrolled in reliance.
    """

    middle_name: str
    """Legal middle name."""

    nationalities: SequenceNotStr[str]
    """ISO 3166-1 alpha-3 codes for all nationalities held."""

    ofac_screen: KyxScreenParam
    """
    Result of a KYC/AML or OFAC screen you performed and are relying on the provider
    to accept, honoured only for developers enrolled in reliance.
    """

    ownership_percentage: int
    """Percentage of the business this person owns."""

    phone: str
    """Phone number in E.164 format."""

    place_of_birth: KYBPlaceOfBirthParam
    """Place of birth for an associated person."""

    relationship_established_at: str
    """Date the relationship with the business was established, in YYYY-MM-DD format."""

    title: str
    """Job title. Required when has_control is true."""

    transliterated_first_name: str
    """Latin-1 transliteration of the first name. Required for non-Latin-1 names."""

    transliterated_last_name: str
    """Latin-1 transliteration of the last name. Required for non-Latin-1 names."""

    transliterated_middle_name: str
    """Latin-1 transliteration of the middle name. Required for non-Latin-1 names."""

    transliterated_residential_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    verified_database_at: Annotated[Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")]
    """When you verified this person against a database source (ISO 8601)."""

    verified_govid_at: Annotated[Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")]
    """When you verified the government ID for this person (ISO 8601)."""

    verified_proof_of_address_at: Annotated[
        Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")
    ]
    """When you verified proof of address for this person (ISO 8601)."""
