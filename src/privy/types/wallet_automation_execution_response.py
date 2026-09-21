# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .wallet_automation_execution_status import WalletAutomationExecutionStatus

__all__ = ["WalletAutomationExecutionResponse"]


class WalletAutomationExecutionResponse(BaseModel):
    """A record of a single automation execution created by a deposit."""

    id: str

    automation_attachment_id: Optional[str] = None

    completed_at: Optional[str] = None

    created_at: str

    failed_at: Optional[str] = None

    failure_reason: Optional[str] = None

    status: WalletAutomationExecutionStatus
    """Execution lifecycle status."""

    submitted_at: Optional[str] = None

    trigger_asset_address: str

    trigger_block_number: str

    trigger_caip2: str

    trigger_tx_hash: str

    updated_at: str

    wallet_action_id: Optional[str] = None

    wallet_id: str
