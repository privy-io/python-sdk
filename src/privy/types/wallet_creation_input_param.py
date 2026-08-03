# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .wallet_chain_type import WalletChainType
from .wallet_creation_additional_signer_item_param import WalletCreationAdditionalSignerItemParam

__all__ = ["WalletCreationInputParam"]


class WalletCreationInputParam(TypedDict, total=False):
    """
    The fields on wallet creation that can be specified when creating a user-controlled embedded server wallet.
    """

    chain_type: Required[WalletChainType]
    """The wallet chain types."""

    additional_signers: Iterable[WalletCreationAdditionalSignerItemParam]
    """Additional signers for the wallet."""

    create_smart_wallet: bool
    """Create a smart wallet with this wallet as the signer.

    Only supported for wallets with `chain_type: "ethereum"`.
    """

    external_id: str
    """A customer-provided identifier for mapping to external systems.

    Write-once, set only at creation. Must be alphanumeric, hyphens, or underscores,
    max 64 characters.
    """

    policy_ids: SequenceNotStr[str]
    """Policy IDs to enforce on the wallet.

    Currently, only one policy is supported per wallet.
    """
