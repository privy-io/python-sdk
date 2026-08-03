# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .address import Address
from .wallet_chain_type import WalletChainType

__all__ = ["WalletListParams"]


class WalletListParams(TypedDict, total=False):
    address: Address
    """A blockchain wallet address.

    Ethereum addresses are normalized to EIP-55 checksum format. Solana addresses
    are validated as base58. All other chain addresses (Stellar, Tron, Sui, Aptos,
    etc.) are accepted as-is.
    """

    authorization_key: str
    """Filter wallets by authorization public key.

    Returns wallets owned by key quorums that include the specified P-256 public key
    (base64-encoded DER format). Cannot be used together with user_id.
    """

    chain_type: WalletChainType
    """The wallet chain types."""

    cursor: str

    entity_id: str
    """Filter wallets by the entity ID the wallet is attributed to."""

    external_id: str
    """Filter wallets by external ID."""

    include_archived: bool
    """Include archived wallets in lookup. Defaults to false."""

    limit: Optional[float]

    user_id: str
    """Filter wallets by user ID. Cannot be used together with authorization_key."""
