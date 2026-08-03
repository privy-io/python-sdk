# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .owner_id_input import OwnerIDInput
from .owner_input_param import OwnerInputParam
from .policy_rule_request_body_param import PolicyRuleRequestBodyParam

__all__ = ["IntentUpdatePolicyParams"]


class IntentUpdatePolicyParams(TypedDict, total=False):
    name: str
    """Name to assign to policy."""

    owner: Optional[OwnerInputParam]
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput]
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    rules: Iterable[PolicyRuleRequestBodyParam]

    privy_request_expiry: Annotated[str, PropertyInfo(alias="privy-request-expiry")]
    """Request expiry.

    Value is a Unix timestamp in milliseconds representing the deadline by which the
    request must be processed.
    """
