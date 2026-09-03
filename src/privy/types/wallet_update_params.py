# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WalletUpdateParams", "AdditionalSigner", "Owner"]


class WalletUpdateParams(TypedDict, total=False):
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
    """New policy IDs to enforce on the wallet.

    Currently, only one policy is supported per wallet.
    """

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """


class AdditionalSigner(TypedDict, total=False):
    override_policy_ids: Required[List[str]]

    signer_id: Required[str]


class Owner(TypedDict, total=False):
    public_key: Required[str]
