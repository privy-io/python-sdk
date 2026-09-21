# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .automation_action_config_input_param import AutomationActionConfigInputParam
from .automation_trigger_config_input_param import AutomationTriggerConfigInputParam

__all__ = ["AutomationConfigInputParam"]


class AutomationConfigInputParam(TypedDict, total=False):
    """
    Full configuration for a wallet automation (trigger + action) accepting human-readable aliases.
    """

    action: Required[AutomationActionConfigInputParam]
    """Configuration for an automation action (input form with alias support)."""

    trigger: Required[AutomationTriggerConfigInputParam]
    """Trigger configuration for deposit events (input form with alias support)."""
