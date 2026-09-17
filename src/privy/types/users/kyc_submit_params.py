# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..kyx_provider import KyxProvider
from ..kyx_environment import KyxEnvironment
from ..kyx_endorsement_name import KyxEndorsementName
from ..kyc_submit_data_param import KYCSubmitDataParam

__all__ = ["KYCSubmitParams"]


class KYCSubmitParams(TypedDict, total=False):
    data: Required[KYCSubmitDataParam]
    """KYC verification data for headless submission."""

    provider: Required[KyxProvider]
    """KYC/KYB provider identifier."""

    client_agreement_id: str
    """Client-side agreement ID for ToS acceptance."""

    endorsements: SequenceNotStr[KyxEndorsementName]
    """Endorsements to request during KYC."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""
