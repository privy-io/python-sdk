# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutomationEarnDepositActionConfig"]


class AutomationEarnDepositActionConfig(BaseModel):
    """Action configuration for depositing into an Earn vault."""

    type: Literal["earn_deposit"]

    vault_id: str
