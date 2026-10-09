# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .kyx_screen_param import KyxScreenParam
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

    kyc_screen: KyxScreenParam
    """
    Result of a KYC/AML or OFAC screen you performed and are relying on the provider
    to accept, honoured only for developers enrolled in reliance.
    """

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

    ofac_screen: KyxScreenParam
    """
    Result of a KYC/AML or OFAC screen you performed and are relying on the provider
    to accept, honoured only for developers enrolled in reliance.
    """

    phone: str
    """Phone number in E.164 format."""

    residential_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    stripe_link_shared_data_id: str
    """
    Stripe Link shared data ID that supplies name, date of birth, address, and US
    SSN (omit those fields); retrieval errors surface in endorsements[].issues.
    """

    transliterated_first_name: str
    """Latin-1 transliteration of the first name. Required for non-Latin-1 names."""

    transliterated_last_name: str
    """Latin-1 transliteration of the last name. Required for non-Latin-1 names."""

    transliterated_middle_name: str
    """Latin-1 transliteration of the middle name. Required for non-Latin-1 names."""

    transliterated_residential_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""

    verified_database_at: Annotated[Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")]
    """
    When you verified the user against a database source (ISO 8601), which loosens
    the identifying-document requirement under reliance.
    """

    verified_govid_at: Annotated[Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")]
    """
    When you verified the government ID (ISO 8601), which loosens the
    identifying-document requirement under reliance.
    """

    verified_proof_of_address_at: Annotated[
        Union[Union[str, datetime], Union[str, date]], PropertyInfo(format="iso8601")
    ]
    """
    When you verified proof of address (ISO 8601), required for EEA customers and
    SEPA rails under reliance.
    """
