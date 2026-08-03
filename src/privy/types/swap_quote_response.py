# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .gas import Gas
from .._models import BaseModel
from .fee_line_item import FeeLineItem

__all__ = ["SwapQuoteResponse"]


class SwapQuoteResponse(BaseModel):
    """Pricing data for a token swap."""

    caip2: str
    """Chain identifier."""

    est_output_amount: str
    """Estimated amount of output token in base units."""

    gas_estimate: str
    """Estimated gas cost in base units of the native token.

    @deprecated For cross-chain swaps, use estimated_gas instead.
    """

    input_amount: str
    """Amount of input token in base units."""

    input_token: str
    """Token address being sold."""

    minimum_output_amount: str
    """Minimum output amount accounting for slippage, in base units."""

    output_token: str
    """Token address being bought."""

    destination_caip2: Optional[str] = None
    """Destination chain CAIP-2 identifier for cross-chain swaps.

    Only present for cross-chain swaps.
    """

    estimated_fees: Optional[List[FeeLineItem]] = None
    """Estimated fees for the swap. Only present for cross-chain swaps."""

    estimated_gas: Optional[Gas] = None
    """Gas cost for a blockchain action.

    Includes both raw base-unit amount and a human-readable decimal string, plus the
    gas token symbol.
    """

    expires_at: Optional[float] = None
    """Quote expiry as Unix timestamp (seconds). Only present for cross-chain quotes."""
