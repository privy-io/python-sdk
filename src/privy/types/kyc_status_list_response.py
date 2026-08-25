# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .kyc_status_response import KYCStatusResponse

__all__ = ["KYCStatusListResponse"]


class KYCStatusListResponse(BaseModel):
    """List of KYC status snapshots, one per configured provider/environment."""

    kyc_statuses: List[KYCStatusResponse]

    next_cursor: Optional[str] = None
