# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .policy_intent_delete_request_body import PolicyIntentDeleteRequestBody

__all__ = ["PolicyIntentDeleteRequestDetails"]


class PolicyIntentDeleteRequestDetails(BaseModel):
    """Request details for deleting a policy via intent."""

    method: Literal["DELETE"]

    url: str

    body: Optional[PolicyIntentDeleteRequestBody] = None
    """Empty request body for a policy delete intent."""
