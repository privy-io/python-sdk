# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .owner_id_input import OwnerIDInput
from .owner_input_param import OwnerInputParam
from .policy_input_param import PolicyInputParam
from .hd_submit_input_param import HDSubmitInputParam
from .additional_signer_input_param import AdditionalSignerInputParam
from .private_key_submit_input_param import PrivateKeySubmitInputParam
from .wallet_entity_assignment_request_body_param import WalletEntityAssignmentRequestBodyParam

__all__ = ["WalletSubmitImportParams", "Wallet"]


class WalletSubmitImportParams(TypedDict, total=False):
    wallet: Required[Wallet]
    """The submission input for importing an HD wallet."""

    additional_signers: AdditionalSignerInputParam
    """Additional signers for the wallet."""

    display_name: str
    """A human-readable label for the wallet."""

    entity: WalletEntityAssignmentRequestBodyParam
    """Request body for assigning an entity to a wallet."""

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

    policy_ids: PolicyInputParam
    """An optional list of up to one policy ID to enforce on the wallet."""


Wallet: TypeAlias = Union[HDSubmitInputParam, PrivateKeySubmitInputParam]
