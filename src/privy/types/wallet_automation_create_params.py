# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .automation_config_input_param import AutomationConfigInputParam

__all__ = ["WalletAutomationCreateParams"]


class WalletAutomationCreateParams(TypedDict, total=False):
    config: Required[AutomationConfigInputParam]
    """
    Full configuration for a wallet automation (trigger + action) accepting
    human-readable aliases.
    """

    owner_id: Required[Optional[str]]

    name: str
