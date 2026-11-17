# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .owner_input import OwnerInput
from .policy_input import PolicyInput
from .owner_id_input import OwnerIDInput
from .additional_signer_input import AdditionalSignerInput

__all__ = ["WalletUpdateRequestBody"]


class WalletUpdateRequestBody(BaseModel):
    """Request body for updating a wallet.

    `owner` and `owner_id` are mutually exclusive.
    """

    additional_signers: Optional[AdditionalSignerInput] = None
    """Additional signers for the wallet."""

    display_name: Optional[str] = None
    """A human-readable label for the wallet. Set to null to clear."""

    external_id: Optional[str] = None
    """A customer-provided identifier for mapping to external systems.

    URL-safe characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be
    changed once set.
    """

    owner: Optional[OwnerInput] = None
    """
    The owner of the resource, specified as a Privy user ID, a P-256 public key, or
    null to remove the current owner.
    """

    owner_id: Optional[OwnerIDInput] = None
    """The key quorum ID to set as the owner of the resource.

    If you provide this, do not specify an owner.
    """

    policy_ids: Optional[PolicyInput] = None
    """An optional list of up to one policy ID to enforce on the wallet."""
