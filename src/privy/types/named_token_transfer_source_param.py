# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamedTokenTransferSourceParam"]


class NamedTokenTransferSourceParam(TypedDict, total=False):
    """Source for a transfer identified by a named asset (e.g.

    "usdc", "eth"). Use this variant for first-class assets maintained by Privy.
    """

    asset: Required[str]
    """The asset to transfer.

    Supported: 'usdc', 'usdb', 'usdt', 'eurc', 'ousd', 'pathusd' (stablecoins),
    'eth' (native Ethereum), 'sol' (native Solana).
    """

    chain: Required[str]
    """The blockchain network on which to perform the transfer.

    Supported chains include: 'tempo', 'ethereum', 'base', 'arbitrum', 'polygon',
    'solana', and their respective testnets.
    """

    amount: str
    """Amount as a decimal string in the token's standard unit (e.g.

    "1.5" for 1.5 USDC, "0.01" for 0.01 ETH). For exact_input, specifies the amount
    to send. Not in the smallest on-chain unit (wei, lamports, etc.). Maximum 100
    characters. Deprecated: use the top-level `amount` field instead.
    """
