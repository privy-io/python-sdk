# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .policy import Policy
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .policy_intent_delete_request_details import PolicyIntentDeleteRequestDetails

__all__ = ["PolicyDeleteIntentResponse"]


class PolicyDeleteIntentResponse(BaseIntentResponse):
    """Response for a policy delete intent"""

    intent_type: Literal["POLICY"]

    request_details: PolicyIntentDeleteRequestDetails
    """Request details for deleting a policy via intent."""

    action_result: Optional[BaseActionResult] = None
    """
    Result of policy delete execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[Policy] = None
    """A policy for controlling wallet operations."""
