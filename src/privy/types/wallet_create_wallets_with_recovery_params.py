# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .wallet_chain_type import WalletChainType
from .policy_input_param import PolicyInputParam
from .linked_account_email_input_param import LinkedAccountEmailInputParam
from .linked_account_custom_jwt_input_param import LinkedAccountCustomJwtInputParam

__all__ = [
    "WalletCreateWalletsWithRecoveryParams",
    "PrimarySigner",
    "RecoveryUser",
    "RecoveryUserLinkedAccount",
    "Wallet",
]


class WalletCreateWalletsWithRecoveryParams(TypedDict, total=False):
    primary_signer: Required[PrimarySigner]

    recovery_user: Required[RecoveryUser]

    wallets: Required[Iterable[Wallet]]


class PrimarySigner(TypedDict, total=False):
    subject_id: Required[str]
    """The JWT subject ID of the user."""


RecoveryUserLinkedAccount: TypeAlias = Union[LinkedAccountEmailInputParam, LinkedAccountCustomJwtInputParam]


class RecoveryUser(TypedDict, total=False):
    linked_accounts: Required[Iterable[RecoveryUserLinkedAccount]]


class Wallet(TypedDict, total=False):
    chain_type: Required[WalletChainType]
    """The wallet chain types."""

    display_name: str
    """A human-readable label for the wallet."""

    external_id: str
    """A customer-provided identifier for mapping to external systems.

    URL-safe characters only ([a-zA-Z0-9_-]), max 64 chars. Write-once: cannot be
    changed after creation.
    """

    policy_ids: PolicyInputParam
    """An optional list of up to one policy ID to enforce on the wallet."""
