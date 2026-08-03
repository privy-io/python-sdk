# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .rule_intent_delete_request_body import RuleIntentDeleteRequestBody

__all__ = ["RuleIntentDeleteRequestDetails"]


class RuleIntentDeleteRequestDetails(BaseModel):
    """Request details for deleting a rule via intent."""

    method: Literal["DELETE"]

    url: str

    body: Optional[RuleIntentDeleteRequestBody] = None
    """Empty request body for a rule delete intent."""
