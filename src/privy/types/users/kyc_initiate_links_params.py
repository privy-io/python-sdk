# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..kyx_provider import KyxProvider
from ..kyx_environment import KyxEnvironment
from ..kyx_endorsement_name import KyxEndorsementName

__all__ = ["KYCInitiateLinksParams"]


class KYCInitiateLinksParams(TypedDict, total=False):
    provider: Required[KyxProvider]
    """KYC/KYB provider identifier."""

    client_agreement_id: str
    """Client-side agreement ID for ToS acceptance."""

    email: str
    """Email address for the KYC session."""

    endorsements: SequenceNotStr[KyxEndorsementName]
    """Endorsements to request during KYC."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""

    redirect_uri: str
    """URI to redirect the user after completing KYC."""
