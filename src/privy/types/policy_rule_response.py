# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .policy_action import PolicyAction
from .policy_method import PolicyMethod
from .policy_condition import PolicyCondition

__all__ = ["PolicyRuleResponse"]


class PolicyRuleResponse(BaseModel):
    """
    A rule that defines the conditions and action to take if the conditions are true.
    """

    id: str

    action: PolicyAction
    """The action to take when a policy rule matches."""

    conditions: List[PolicyCondition]

    method: PolicyMethod
    """Method the rule applies to."""

    name: str
