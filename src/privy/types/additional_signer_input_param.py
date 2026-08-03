# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypeAlias, TypedDict

from .key_quorum_id import KeyQuorumID
from .policy_input_param import PolicyInputParam

__all__ = ["AdditionalSignerInputParam", "AdditionalSignerItemInputParam"]


class AdditionalSignerItemInputParam(TypedDict, total=False):
    """A single additional signer for a wallet, with an optional policy override."""

    signer_id: Required[KeyQuorumID]
    """A unique identifier for a key quorum."""

    override_policy_ids: PolicyInputParam
    """An optional list of up to one policy ID to enforce on the wallet."""


AdditionalSignerInputParam: TypeAlias = List[AdditionalSignerItemInputParam]
