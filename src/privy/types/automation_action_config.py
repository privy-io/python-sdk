# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .automation_swap_action_config import AutomationSwapActionConfig
from .automation_earn_deposit_action_config import AutomationEarnDepositActionConfig

__all__ = ["AutomationActionConfig"]

AutomationActionConfig: TypeAlias = Annotated[
    Union[AutomationSwapActionConfig, AutomationEarnDepositActionConfig], PropertyInfo(discriminator="type")
]
