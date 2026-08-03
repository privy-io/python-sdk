# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .key_quorum_id import KeyQuorumID
from .wallet_chain_type import WalletChainType
from .policy_rule_response import PolicyRuleResponse

__all__ = ["Policy"]


class Policy(BaseModel):
    """A policy for controlling wallet operations."""

    id: str
    """Unique ID of the created policy.

    This will be the primary identifier when using the policy in the future.
    """

    chain_type: WalletChainType
    """The wallet chain types."""

    created_at: float
    """Unix timestamp of when the policy was created in milliseconds."""

    name: str
    """Name to assign to policy."""

    owner_id: Optional[KeyQuorumID] = None
    """A unique identifier for a key quorum."""

    rules: List[PolicyRuleResponse]

    version: Literal["1.0"]
    """Version of the policy. Currently, 1.0 is the only version."""
