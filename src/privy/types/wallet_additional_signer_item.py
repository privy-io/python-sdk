# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .policy_input import PolicyInput
from .key_quorum_id import KeyQuorumID

__all__ = ["WalletAdditionalSignerItem"]


class WalletAdditionalSignerItem(BaseModel):
    """A single additional signer on a wallet, with an optional policy override."""

    signer_id: KeyQuorumID
    """A unique identifier for a key quorum."""

    override_policy_ids: Optional[PolicyInput] = None
    """An optional list of up to one policy ID to enforce on the wallet."""
