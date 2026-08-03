# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PrivyFee"]


class PrivyFee(BaseModel):
    """Estimated fee paid to Privy."""

    amount: str
    """Amount in USD (in decimals)."""

    type: Literal["privy"]

    recipient: Optional[str] = None
