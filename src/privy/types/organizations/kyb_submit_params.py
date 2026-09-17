# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..kyx_provider import KyxProvider
from ..kyx_environment import KyxEnvironment
from ..kyx_endorsement_name import KyxEndorsementName
from ..kyb_submit_data_param import KYBSubmitDataParam

__all__ = ["KYBSubmitParams"]


class KYBSubmitParams(TypedDict, total=False):
    data: Required[KYBSubmitDataParam]
    """KYB verification data for headless submission.

    Fields are individually optional because the provider accepts partial
    submissions and grants endorsements once enough data has arrived; a partial
    submission can be completed by calling the endpoint again.
    """

    provider: Required[KyxProvider]
    """KYC/KYB provider identifier."""

    client_agreement_id: str
    """Client-side agreement ID for ToS acceptance."""

    endorsements: SequenceNotStr[KyxEndorsementName]
    """Endorsements to request during KYB."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""
