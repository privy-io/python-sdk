# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AutomationEarnDepositActionConfigInputParam"]


class AutomationEarnDepositActionConfigInputParam(TypedDict, total=False):
    """Action configuration for depositing into an Earn vault (input form)."""

    type: Required[Literal["earn_deposit"]]

    vault_id: Required[str]
