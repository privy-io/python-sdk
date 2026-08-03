# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .policy_action import PolicyAction
from .policy_method import PolicyMethod
from .owner_id_input import OwnerIDInput
from .owner_input_param import OwnerInputParam
from .wallet_chain_type import WalletChainType
from .policy_condition_param import PolicyConditionParam

__all__ = ["PolicyCreateParams", "Rule"]


class PolicyCreateParams(TypedDict, total=False):
    chain_type: Required[WalletChainType]
    """The wallet chain types."""

    name: Required[str]
    """Name to assign to policy."""

    rules: Required[Iterable[Rule]]

    version: Required[Literal["1.0"]]
    """Version of the policy. Currently, 1.0 is the only version."""

    owner: Optional[OwnerInputParam]
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput]
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    privy_idempotency_key: Annotated[str, PropertyInfo(alias="privy-idempotency-key")]
    """
    Idempotency keys ensure API requests are executed only once within a 24-hour
    window.
    """


class Rule(TypedDict, total=False):
    action: Required[PolicyAction]
    """The action to take when a policy rule matches."""

    conditions: Required[Iterable[PolicyConditionParam]]

    method: Required[PolicyMethod]
    """Method the rule applies to."""

    name: Required[str]

    id: str
