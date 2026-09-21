# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .key_quorum_id import KeyQuorumID
from .automation_config_input_param import AutomationConfigInputParam

__all__ = ["WalletAutomationUpdateParams"]


class WalletAutomationUpdateParams(TypedDict, total=False):
    config: AutomationConfigInputParam
    """
    Full configuration for a wallet automation (trigger + action) accepting
    human-readable aliases.
    """

    enabled: bool

    name: Optional[str]

    owner_id: Optional[KeyQuorumID]
    """A unique identifier for a key quorum."""
