# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .wallet import Wallet
from .._models import BaseModel
from .encrypted_authorization_key import EncryptedAuthorizationKey

__all__ = ["EncryptedWalletAuthenticateResponse"]


class EncryptedWalletAuthenticateResponse(BaseModel):
    """
    The response from authenticating a wallet with HPKE encryption, containing an encrypted authorization key and wallet data.
    """

    encrypted_authorization_key: EncryptedAuthorizationKey
    """HPKE-encrypted authorization key with encapsulated key and ciphertext."""

    expires_at: float
    """The expiration time of the authorization key in milliseconds since the epoch."""

    wallets: List[Wallet]
