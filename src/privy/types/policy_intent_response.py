# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .policy import Policy
from .._models import BaseModel
from .owner_input import OwnerInput
from .owner_id_input import OwnerIDInput
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .policy_rule_request_body import PolicyRuleRequestBody

__all__ = ["PolicyIntentResponse", "PolicyIntentResponseRequestDetails", "PolicyIntentResponseRequestDetailsBody"]


class PolicyIntentResponseRequestDetailsBody(BaseModel):
    name: Optional[str] = None
    """Name to assign to policy."""

    owner: Optional[OwnerInput] = None
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput] = None
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    rules: Optional[List[PolicyRuleRequestBody]] = None


class PolicyIntentResponseRequestDetails(BaseModel):
    """The original policy update request that would be sent to the policy endpoint"""

    body: PolicyIntentResponseRequestDetailsBody

    method: Literal["PATCH"]

    url: str


class PolicyIntentResponse(BaseIntentResponse):
    """Response for a policy intent"""

    intent_type: Literal["POLICY"]

    request_details: PolicyIntentResponseRequestDetails
    """The original policy update request that would be sent to the policy endpoint"""

    action_result: Optional[BaseActionResult] = None
    """
    Result of policy update execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[Policy] = None
    """A policy for controlling wallet operations."""
