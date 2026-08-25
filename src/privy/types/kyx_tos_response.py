# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .kyx_provider import KyxProvider
from .kyx_tos_status import KyxTosStatus
from .kyx_environment import KyxEnvironment

__all__ = ["KyxTosResponse"]


class KyxTosResponse(BaseModel):
    """Response containing a Terms of Service link."""

    environment: KyxEnvironment
    """Provider environment (production or sandbox)."""

    link: str
    """URL for the Terms of Service acceptance page."""

    provider: KyxProvider
    """KYC/KYB provider identifier."""

    status: KyxTosStatus
    """Status of Terms of Service acceptance. Passthrough from the provider."""
