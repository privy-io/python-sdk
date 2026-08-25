# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..kyx_provider import KyxProvider
from ..kyx_environment import KyxEnvironment
from ..kyx_endorsement_name import KyxEndorsementName

__all__ = ["KYBInitiateLinksParams"]


class KYBInitiateLinksParams(TypedDict, total=False):
    email: Required[str]
    """Email address for the organization."""

    provider: Required[KyxProvider]
    """KYC/KYB provider identifier."""

    business_name: str
    """Legal name of the business."""

    client_agreement_id: str
    """Client-side agreement ID for ToS acceptance."""

    endorsements: SequenceNotStr[KyxEndorsementName]
    """Endorsements to request during KYB."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""

    redirect_uri: str
    """URI to redirect after completing KYB."""
