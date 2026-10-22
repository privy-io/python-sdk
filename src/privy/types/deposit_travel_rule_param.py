# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .travel_rule_counterparty_param import TravelRuleCounterpartyParam

__all__ = ["DepositTravelRuleParam"]


class DepositTravelRuleParam(TypedDict, total=False):
    """Travel rule information about who sends deposits into a fiat deposit account."""

    source: Required[TravelRuleCounterpartyParam]
    """The bank-side party to a fiat transfer, for travel rule compliance."""
