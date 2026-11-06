# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .stellar_address import StellarAddress

__all__ = ["DeveloperFee"]


class DeveloperFee(BaseModel):
    """Estimated fee paid to the developer."""

    amount: str
    """Amount in USD (in decimals)."""

    type: Literal["developer"]

    recipient: Optional[StellarAddress] = None
    """
    Stellar account address: an ed25519 public key in StrKey encoding, starting with
    G.
    """
