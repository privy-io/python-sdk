# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .travel_rule_self_counterparty_param import TravelRuleSelfCounterpartyParam
from .travel_rule_business_counterparty_param import TravelRuleBusinessCounterpartyParam
from .travel_rule_individual_counterparty_param import TravelRuleIndividualCounterpartyParam

__all__ = ["TravelRuleCounterpartyParam"]

TravelRuleCounterpartyParam: TypeAlias = Union[
    TravelRuleSelfCounterpartyParam, TravelRuleIndividualCounterpartyParam, TravelRuleBusinessCounterpartyParam
]
