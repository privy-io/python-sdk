# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .wallet_automation_execution_response import WalletAutomationExecutionResponse

__all__ = ["WalletAutomationExecutionListResponse"]


class WalletAutomationExecutionListResponse(BaseModel):
    """Paginated list of wallet automation executions."""

    data: List[WalletAutomationExecutionResponse]
    """Items in this page."""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null when there are no further pages."""
