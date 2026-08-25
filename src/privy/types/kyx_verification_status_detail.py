# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .kyx_verification_status import KyxVerificationStatus

__all__ = ["KyxVerificationStatusDetail"]


class KyxVerificationStatusDetail(BaseModel):
    """Verification status detail for a KYC or KYB check."""

    status: KyxVerificationStatus
    """Status of KYC/KYB verification. Passthrough from the provider."""

    link: Optional[str] = None
    """Verification link, if applicable."""

    rejection_reasons: Optional[List[str]] = None
    """Reasons for rejection, if status is closed or action_required."""
