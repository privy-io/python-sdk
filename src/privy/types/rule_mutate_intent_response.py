# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .policy import Policy
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .policy_rule_response import PolicyRuleResponse
from .rule_intent_request_details import RuleIntentRequestDetails

__all__ = ["RuleMutateIntentResponse"]


class RuleMutateIntentResponse(BaseIntentResponse):
    """Response for a create or update rule intent"""

    intent_type: Literal["RULE"]

    request_details: RuleIntentRequestDetails
    """The original rule request.

    Method is POST (create), PATCH (update), or DELETE (delete)
    """

    action_result: Optional[BaseActionResult] = None
    """Result of rule execution (only present if status is 'executed' or 'failed')"""

    current_resource_data: Optional[PolicyRuleResponse] = None
    """
    A rule that defines the conditions and action to take if the conditions are
    true.
    """

    policy: Optional[Policy] = None
    """A policy for controlling wallet operations."""
