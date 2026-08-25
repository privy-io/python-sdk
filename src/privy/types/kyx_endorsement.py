# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .kyx_endorsement_name import KyxEndorsementName
from .kyx_endorsement_status import KyxEndorsementStatus

__all__ = ["KyxEndorsement"]


class KyxEndorsement(BaseModel):
    """An endorsement with its approval status and missing requirements."""

    missing: Optional[List[str]] = None
    """Missing requirements, or null if complete."""

    name: KyxEndorsementName
    """Endorsement identifier."""

    status: KyxEndorsementStatus
    """Status of an endorsement. Passthrough from the provider."""
