# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .travel_rule_counterparty_param import TravelRuleCounterpartyParam

__all__ = ["PayoutTravelRuleParam"]


class PayoutTravelRuleParam(TypedDict, total=False):
    """Travel rule information about who receives a payout."""

    destination: Required[TravelRuleCounterpartyParam]
    """The bank-side party to a fiat transfer, for travel rule compliance."""
