# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .verification_address_param import VerificationAddressParam
from .verification_document_param import VerificationDocumentParam

__all__ = ["KYCSubmitDataParam"]


class KYCSubmitDataParam(TypedDict, total=False):
    """KYC verification data for headless submission."""

    date_of_birth: str
    """Date of birth in YYYY-MM-DD format."""

    email: str
    """Email address."""

    first_name: str
    """Legal first name."""

    identifying_information: Iterable[VerificationDocumentParam]
    """Identifying documents."""

    last_name: str
    """Legal last name."""

    middle_name: str
    """Legal middle name."""

    nationalities: SequenceNotStr[str]
    """ISO 3166-1 alpha-3 codes for all nationalities held."""

    nonresident_alien_attestation: bool
    """
    Attests the user is a nonresident alien to satisfy identification without a US
    tax ID (must be enabled for you).
    """

    phone: str
    """Phone number in E.164 format."""

    residential_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    transliterated_first_name: str
    """Latin-1 transliteration of the first name. Required for non-Latin-1 names."""

    transliterated_last_name: str
    """Latin-1 transliteration of the last name. Required for non-Latin-1 names."""

    transliterated_middle_name: str
    """Latin-1 transliteration of the middle name. Required for non-Latin-1 names."""

    transliterated_residential_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""
