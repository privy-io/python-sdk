# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CryptoDepositAsset"]


class CryptoDepositAsset(BaseModel):
    """An asset on a chain.

    Uses a human-readable alias (usdc, base) when one is on file, otherwise the raw asset address and CAIP-2.
    """

    asset: str
    """Known alias (usdc) or raw asset address."""

    chain: str
    """Known alias (base) or CAIP-2."""
