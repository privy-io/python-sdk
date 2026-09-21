# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .swap_attachment_params import SwapAttachmentParams
from .wallet_automation_status import WalletAutomationStatus

__all__ = ["WalletAutomationAttachmentResponse"]


class WalletAutomationAttachmentResponse(BaseModel):
    """A wallet automation attachment linking an automation to a specific wallet."""

    id: str

    automation_id: str

    created_at: str

    params: Optional[SwapAttachmentParams] = None
    """Per-attachment parameters for swap automations."""

    status: WalletAutomationStatus
    """Automation lifecycle state: 'enabled' = running, 'disabled' = not running."""

    updated_at: str

    wallet_id: str
