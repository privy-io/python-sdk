# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "WalletCreateWalletsWithRecoveryParams",
    "PrimarySigner",
    "RecoveryUser",
    "RecoveryUserLinkedAccount",
    "RecoveryUserLinkedAccountUnionMember0",
    "RecoveryUserLinkedAccountUnionMember1",
    "Wallet",
]


class WalletCreateWalletsWithRecoveryParams(TypedDict, total=False):
    primary_signer: Required[PrimarySigner]

    recovery_user: Required[RecoveryUser]

    wallets: Required[Iterable[Wallet]]


class PrimarySigner(TypedDict, total=False):
    subject_id: Required[str]
    """The JWT subject ID of the user."""


class RecoveryUserLinkedAccountUnionMember0(TypedDict, total=False):
    address: Required[str]
    """The email address of the user."""

    type: Required[Literal["email"]]


class RecoveryUserLinkedAccountUnionMember1(TypedDict, total=False):
    custom_user_id: Required[str]
    """The JWT subject ID of the user."""

    type: Required[Literal["custom_auth"]]


RecoveryUserLinkedAccount: TypeAlias = Union[
    RecoveryUserLinkedAccountUnionMember0, RecoveryUserLinkedAccountUnionMember1
]


class RecoveryUser(TypedDict, total=False):
    linked_accounts: Required[Iterable[RecoveryUserLinkedAccount]]


class Wallet(TypedDict, total=False):
    chain_type: Required[Literal["solana", "ethereum", "cosmos", "stellar", "sui", "tron"]]
    """Chain type of the wallet. "ethereum" supports any EVM-compatible network."""

    policy_ids: List[str]
    """List of policy IDs for policies that should be enforced on the wallet.

    Currently, only one policy is supported per wallet.
    """
