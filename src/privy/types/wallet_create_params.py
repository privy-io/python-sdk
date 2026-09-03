# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["WalletCreateParams", "AdditionalSigner", "Owner", "OwnerPublicKey", "OwnerUserID"]


class WalletCreateParams(TypedDict, total=False):
    chain_type: Required[Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"]]
    """Chain type of the wallet. "ethereum" supports any EVM-compatible network."""

    additional_signers: Iterable[AdditionalSigner]
    """Additional signers for the wallet."""

    owner: Optional[Owner]
    """The P-256 public key of the owner of the wallet.

    If you provide this, do not specify an owner_id as it will be generated
    automatically.
    """

    owner_id: Optional[str]
    """The key quorum ID to set as the owner of the wallet.

    If you provide this, do not specify an owner.
    """

    policy_ids: List[str]
    """List of policy IDs for policies that should be enforced on the wallet.

    Currently, only one policy is supported per wallet.
    """

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """

    privy_idempotency_key: Annotated[str, PropertyInfo(alias="privy-idempotency-key")]
    """
    Idempotency keys ensure API requests are executed only once within a 24-hour
    window.
    """


class AdditionalSigner(TypedDict, total=False):
    override_policy_ids: Required[List[str]]

    signer_id: Required[str]


class OwnerPublicKey(TypedDict, total=False):
    public_key: Required[str]


class OwnerUserID(TypedDict, total=False):
    user_id: Required[str]


Owner: TypeAlias = Union[OwnerPublicKey, OwnerUserID]
