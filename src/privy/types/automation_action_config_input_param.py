# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .automation_swap_action_config_input_param import AutomationSwapActionConfigInputParam
from .automation_earn_deposit_action_config_input_param import AutomationEarnDepositActionConfigInputParam

__all__ = ["AutomationActionConfigInputParam"]

AutomationActionConfigInputParam: TypeAlias = Union[
    AutomationSwapActionConfigInputParam, AutomationEarnDepositActionConfigInputParam
]
