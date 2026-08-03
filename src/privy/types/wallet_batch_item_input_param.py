# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .owner_id_input import OwnerIDInput
from .owner_input_param import OwnerInputParam
from .wallet_chain_type import WalletChainType
from .additional_signer_input_param import AdditionalSignerInputParam

__all__ = ["WalletBatchItemInputParam"]


class WalletBatchItemInputParam(TypedDict, total=False):
    """Input for a single wallet in a batch creation request."""

    chain_type: Required[WalletChainType]
    """The wallet chain types."""

    additional_signers: AdditionalSignerInputParam
    """Additional signers for the wallet."""

    display_name: str
    """A human-readable label for the wallet."""

    external_id: str
    """A customer-provided identifier for mapping to external systems.

    URL-safe characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be
    changed after creation.
    """

    owner: Optional[OwnerInputParam]
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput]
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    policy_ids: SequenceNotStr[str]
    """List of policy IDs for policies that should be enforced on the wallet.

    Currently, only one policy is supported per wallet.
    """
