# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .hpke_encryption import HpkeEncryption
from .wallet_import_supported_chains import WalletImportSupportedChains

__all__ = ["HDInitInputParam"]


class HDInitInputParam(TypedDict, total=False):
    """The input for HD wallets."""

    address: Required[str]
    """The address of the wallet to import."""

    chain_type: Required[WalletImportSupportedChains]
    """The chain type of the wallet to import.

    Supports `ethereum`, `solana`, `stellar`, `tron`, `sui`, and `aptos`.
    """

    encryption_type: Required[HpkeEncryption]
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""

    entropy_type: Required[Literal["hd"]]
    """The entropy type of the wallet to import."""

    index: Required[int]
    """The index of the wallet to import."""
