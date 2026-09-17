# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
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

    documents: Iterable[KYBIndividualDocumentParam]
    """Supporting documents for this person, such as proof of address."""

    is_director: bool
    """Whether this person is a director."""

    middle_name: str
    """Legal middle name."""

    nationalities: SequenceNotStr[str]
    """ISO 3166-1 alpha-3 codes for all nationalities held."""

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
