# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .automation_config import AutomationConfig
from .wallet_automation_status import WalletAutomationStatus

__all__ = ["WalletAutomationResponse"]


class WalletAutomationResponse(BaseModel):
    """A wallet automation."""

    id: str

    app_id: str

    config: AutomationConfig
    """Full configuration for a wallet automation (trigger + action)."""

    created_at: str

    name: Optional[str] = None

    owner_id: Optional[str] = None

    status: WalletAutomationStatus
    """Automation lifecycle state: 'enabled' = running, 'disabled' = not running."""

    updated_at: str
