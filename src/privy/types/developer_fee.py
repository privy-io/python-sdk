# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeveloperFee"]


class DeveloperFee(BaseModel):
    """Estimated fee paid to the developer."""

    amount: str
    """Amount in USD (in decimals)."""

    type: Literal["developer"]

    recipient: Optional[str] = None
