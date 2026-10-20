# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .policy import Policy
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .policy_intent_request_details_union import PolicyIntentRequestDetailsUnion

__all__ = ["PolicyIntentResponse"]


class PolicyIntentResponse(BaseIntentResponse):
    """Response for a policy intent"""

    intent_type: Literal["POLICY"]

    request_details: PolicyIntentRequestDetailsUnion
    """The original policy request. Method is PATCH (update) or DELETE (delete)."""

    action_result: Optional[BaseActionResult] = None
    """Result of policy execution (only present if status is 'executed' or 'failed')"""

    current_resource_data: Optional[Policy] = None
    """A policy for controlling wallet operations."""
