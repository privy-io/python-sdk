# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .address import Address

__all__ = ["WalletGetWalletByAddressParams"]


class WalletGetWalletByAddressParams(TypedDict, total=False):
    address: Required[Address]
    """A blockchain wallet address.

    Ethereum addresses are normalized to EIP-55 checksum format. Solana addresses
    are validated as base58. All other chain addresses (Stellar, Tron, Sui, Aptos,
    etc.) are accepted as-is.
    """

    include_archived: bool
    """Include archived wallets in lookup.

    Defaults to false (archived wallets return 404).
    """
