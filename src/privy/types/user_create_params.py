# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .key_quorum_id import KeyQuorumID
from .wallet_chain_type import WalletChainType
from .custom_metadata_param import CustomMetadataParam
from .linked_account_input_param import LinkedAccountInputParam

__all__ = ["UserCreateParams", "Wallet", "WalletAdditionalSigner"]


class UserCreateParams(TypedDict, total=False):
    linked_accounts: Required[Iterable[LinkedAccountInputParam]]

    custom_metadata: CustomMetadataParam
    """Custom metadata associated with the user."""

    wallets: Iterable[Wallet]
    """Wallets to create for the user."""


class WalletAdditionalSigner(TypedDict, total=False):
    signer_id: Required[KeyQuorumID]
    """A unique identifier for a key quorum."""

    override_policy_ids: SequenceNotStr[str]
    """The array of policy IDs that will be applied to wallet requests.

    If specified, this will override the base policy IDs set on the wallet.
    Currently, only one policy is supported per signer.
    """


class Wallet(TypedDict, total=False):
    chain_type: Required[WalletChainType]
    """The wallet chain types."""

    additional_signers: Iterable[WalletAdditionalSigner]
    """Additional signers for the wallet."""

    create_smart_wallet: bool
    """Create a smart wallet with this wallet as the signer.

    Only supported for wallets with `chain_type: "ethereum"`.
    """

    policy_ids: SequenceNotStr[str]
    """Policy IDs to enforce on the wallet.

    Currently, only one policy is supported per wallet.
    """
