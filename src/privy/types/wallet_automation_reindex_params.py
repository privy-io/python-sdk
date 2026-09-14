# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .wallet_automation_reindex_caip_2_param import WalletAutomationReindexCaip2Param

__all__ = ["WalletAutomationReindexParams"]


class WalletAutomationReindexParams(TypedDict, total=False):
    asset_address: Required[str]
    """Asset contract address to check; the native asset uses `native`."""

    caip2: WalletAutomationReindexCaip2Param
    """
    An EVM, Solana, or Tron CAIP-2 chain identifier supported by wallet automation
    reindex.
    """

    chain: str
    """Human-readable chain name to check. Specify exactly one of `caip2` or `chain`."""

    deposit_address: str
    """On-chain deposit address of the wallet to reindex.

    Must match the resolved wallet's address if `wallet_id` is also provided.
    """

    wallet_id: str
    """Privy wallet ID to reindex.

    Takes precedence over `deposit_address` when both are supplied.
    """
