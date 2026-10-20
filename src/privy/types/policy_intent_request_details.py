# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .owner_input import OwnerInput
from .owner_id_input import OwnerIDInput
from .policy_rule_request_body import PolicyRuleRequestBody

__all__ = ["PolicyIntentRequestDetails", "Body"]


class Body(BaseModel):
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


class PolicyIntentRequestDetails(BaseModel):
    """Request details for a policy intent."""

    body: Body

    method: Literal["PATCH"]

    url: str
