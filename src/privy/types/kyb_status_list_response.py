# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .kyb_status_response import KYBStatusResponse

__all__ = ["KYBStatusListResponse"]


class KYBStatusListResponse(BaseModel):
    """List of KYB status snapshots, one per configured provider/environment."""

    kyb_statuses: List[KYBStatusResponse]

    next_cursor: Optional[str] = None
