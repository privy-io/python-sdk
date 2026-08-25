# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .kyx_capability_status import KyxCapabilityStatus

__all__ = ["KyxCapabilities"]


class KyxCapabilities(BaseModel):
    """Capability statuses for the customer."""

    payin_crypto: KyxCapabilityStatus
    """Status of a capability. Passthrough from the provider."""

    payin_fiat: KyxCapabilityStatus
    """Status of a capability. Passthrough from the provider."""

    payout_crypto: KyxCapabilityStatus
    """Status of a capability. Passthrough from the provider."""

    payout_fiat: KyxCapabilityStatus
    """Status of a capability. Passthrough from the provider."""
