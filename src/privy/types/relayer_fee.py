# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RelayerFee"]


class RelayerFee(BaseModel):
    """Estimated fee paid to the relayer."""

    amount: str
    """Amount in USD (in decimals)."""

    type: Literal["relayer"]

    recipient: Optional[str] = None
