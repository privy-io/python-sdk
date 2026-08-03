# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .owner_id_input import OwnerIDInput
from .owner_input_param import OwnerInputParam
from .wallet_chain_type import WalletChainType
from .policy_input_param import PolicyInputParam
from .additional_signer_input_param import AdditionalSignerInputParam

__all__ = ["WalletCreateParams", "Entity"]


class WalletCreateParams(TypedDict, total=False):
    chain_type: Required[WalletChainType]
    """The wallet chain types."""

    additional_signers: AdditionalSignerInputParam
    """Additional signers for the wallet."""

    display_name: str
    """A human-readable label for the wallet."""

    entity: Entity
    """The entity the wallet is attributed to."""

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

    privy_idempotency_key: Annotated[str, PropertyInfo(alias="privy-idempotency-key")]
    """
    Idempotency keys ensure API requests are executed only once within a 24-hour
    window.
    """


class Entity(TypedDict, total=False):
    """The entity the wallet is attributed to."""

    id: Required[str]

    type: Required[Literal["user"]]
