# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .policy_action import PolicyAction
from .policy_method import PolicyMethod
from .policy_condition_param import PolicyConditionParam

__all__ = ["PolicyRuleRequestBodyParam"]


class PolicyRuleRequestBodyParam(TypedDict, total=False):
    """The rules that apply to each method the policy covers."""

    action: Required[PolicyAction]
    """The action to take when a policy rule matches."""

    conditions: Required[Iterable[PolicyConditionParam]]

    method: Required[PolicyMethod]
    """Method the rule applies to."""

    name: Required[str]
