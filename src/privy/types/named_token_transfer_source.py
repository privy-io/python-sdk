# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NamedTokenTransferSource"]


class NamedTokenTransferSource(BaseModel):
    """Source for a transfer identified by a named asset (e.g.

    "usdc", "eth"). Use this variant for first-class assets maintained by Privy.
    """

    asset: str
    """The asset to transfer.

    Supported: 'usdc', 'usdb', 'usdt', 'pathusd' (stablecoins), 'eth' (native
    Ethereum), 'sol' (native Solana).
    """

    chain: str
    """The blockchain network on which to perform the transfer.

    Supported chains include: 'tempo', 'ethereum', 'base', 'arbitrum', 'polygon',
    'solana', and their respective testnets.
    """

    amount: Optional[str] = None
    """Amount as a decimal string in the token's standard unit (e.g.

    "1.5" for 1.5 USDC, "0.01" for 0.01 ETH). For exact_input, specifies the amount
    to send. Not in the smallest on-chain unit (wei, lamports, etc.). Maximum 100
    characters. Deprecated: use the top-level `amount` field instead.
    """
