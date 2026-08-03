# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .key_quorum_id import KeyQuorumID

__all__ = ["WalletCreationAdditionalSignerItemParam"]


class WalletCreationAdditionalSignerItemParam(TypedDict, total=False):
    """An additional signer configuration for a wallet."""

    signer_id: Required[KeyQuorumID]
    """A unique identifier for a key quorum."""

    override_policy_ids: SequenceNotStr[str]
    """The array of policy IDs that will be applied to wallet requests.

    If specified, this will override the base policy IDs set on the wallet.
    Currently, only one policy is supported per signer.
    """
