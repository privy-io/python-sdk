# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .wallet import Wallet
from .._models import BaseModel

__all__ = ["RawWalletAuthenticateResponse"]


class RawWalletAuthenticateResponse(BaseModel):
    """
    The response from authenticating a wallet without encryption, containing a raw authorization key and wallet data.
    """

    authorization_key: str
    """The raw authorization key data."""

    expires_at: float
    """The expiration time of the authorization key in milliseconds since the epoch."""

    wallets: List[Wallet]
