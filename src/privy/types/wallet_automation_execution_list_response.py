# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .wallet_automation_execution_response import WalletAutomationExecutionResponse

__all__ = ["WalletAutomationExecutionListResponse"]


class WalletAutomationExecutionListResponse(BaseModel):
    """Paginated list of wallet automation executions."""

    data: List[WalletAutomationExecutionResponse]

    next_cursor: Optional[str] = None
