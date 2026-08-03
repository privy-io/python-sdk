# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .policy_action import PolicyAction
from .policy_method import PolicyMethod
from .policy_condition_param import PolicyConditionParam

__all__ = ["IntentCreatePolicyRuleParams"]


class IntentCreatePolicyRuleParams(TypedDict, total=False):
    action: Required[PolicyAction]
    """The action to take when a policy rule matches."""

    conditions: Required[Iterable[PolicyConditionParam]]

    method: Required[PolicyMethod]
    """Method the rule applies to."""

    name: Required[str]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
