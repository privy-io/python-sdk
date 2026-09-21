# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .wallet_automation_response import WalletAutomationResponse

__all__ = ["WalletAutomationListResponse"]


class WalletAutomationListResponse(BaseModel):
    """Paginated list of wallet automations."""

    data: List[WalletAutomationResponse]

    next_cursor: Optional[str] = None
