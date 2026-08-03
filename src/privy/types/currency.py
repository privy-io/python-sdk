# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .caip_2 import Caip2
from .._models import BaseModel
from .currency_asset import CurrencyAsset

__all__ = ["Currency"]


class Currency(BaseModel):
    """A crypto currency identified by a CAIP-2 chain ID and optional asset."""

    chain: Caip2
    """A valid CAIP-2 chain ID (e.g.

    'eip155:4217' for Tempo, 'eip155:1' for Ethereum).
    """

    asset: Optional[CurrencyAsset] = None
    """A currency asset type."""
