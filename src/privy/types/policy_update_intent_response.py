# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .policy import Policy
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .policy_intent_request_details import PolicyIntentRequestDetails

__all__ = ["PolicyUpdateIntentResponse"]


class PolicyUpdateIntentResponse(BaseIntentResponse):
    """Response for a policy update intent"""

    intent_type: Literal["POLICY"]

    request_details: PolicyIntentRequestDetails
    """Request details for a policy intent."""

    action_result: Optional[BaseActionResult] = None
    """
    Result of policy update execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[Policy] = None
    """A policy for controlling wallet operations."""
