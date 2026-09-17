# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

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

    phone: str
    """Phone number in E.164 format."""

    residential_address: VerificationAddressParam
    """A postal address used in KYC and KYB data submission."""
