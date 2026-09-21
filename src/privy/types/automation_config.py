# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .automation_action_config import AutomationActionConfig
from .automation_trigger_config import AutomationTriggerConfig

__all__ = ["AutomationConfig"]


class AutomationConfig(BaseModel):
    """Full configuration for a wallet automation (trigger + action)."""

    action: AutomationActionConfig
    """Configuration for an automation action."""

    trigger: AutomationTriggerConfig
    """Trigger configuration for deposit events."""
