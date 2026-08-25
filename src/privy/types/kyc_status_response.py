# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .kyx_provider import KyxProvider
from .kyx_endorsement import KyxEndorsement
from .kyx_environment import KyxEnvironment
from .kyx_capabilities import KyxCapabilities
from .kyx_provider_status import KyxProviderStatus
from .kyx_tos_status_detail import KyxTosStatusDetail
from .kyx_verification_status_detail import KyxVerificationStatusDetail

__all__ = ["KYCStatusResponse"]


class KYCStatusResponse(BaseModel):
    """Full KYC status for a user with a given provider."""

    capabilities: KyxCapabilities
    """Capability statuses for the customer."""

    endorsements: List[KyxEndorsement]

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""

    future_requirements_due: List[str]
    """Items that will be required in the future."""

    kyc: KyxVerificationStatusDetail
    """Verification status detail for a KYC or KYB check."""

    provider: KyxProvider
    """KYC/KYB provider identifier."""

    requirements_due: List[str]
    """Top-level items still needed (e.g. link a bank account)."""

    status: KyxProviderStatus
    """KYC/KYB status for the user."""

    tos: KyxTosStatusDetail
    """Terms of Service acceptance status for a KYC or KYB flow."""
