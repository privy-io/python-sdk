# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .policy_rule_request_body import PolicyRuleRequestBody

__all__ = ["RuleIntentCreateRequestDetails"]


class RuleIntentCreateRequestDetails(BaseModel):
    """Request details for creating a rule via intent."""

    body: PolicyRuleRequestBody
    """The rules that apply to each method the policy covers."""

    method: Literal["POST"]

    url: str
