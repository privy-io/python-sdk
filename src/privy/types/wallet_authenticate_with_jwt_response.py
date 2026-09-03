# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from .wallet import Wallet
from .._models import BaseModel

__all__ = [
    "WalletAuthenticateWithJwtResponse",
    "WithEncryption",
    "WithEncryptionEncryptedAuthorizationKey",
    "WithoutEncryption",
]


class WithEncryptionEncryptedAuthorizationKey(BaseModel):
    ciphertext: str
    """
    The encrypted authorization key corresponding to the user's current
    authentication session.
    """

    encapsulated_key: str
    """Base64-encoded ephemeral public key used in the HPKE encryption process.

    Required for decryption.
    """

    encryption_type: Literal["HPKE"]
    """The encryption type used. Currently only supports HPKE."""


class WithEncryption(BaseModel):
    encrypted_authorization_key: WithEncryptionEncryptedAuthorizationKey
    """The encrypted authorization key data."""

    expires_at: float
    """The expiration time of the authorization key in seconds since the epoch."""

    wallets: List[Wallet]
    """The wallets that the signer has access to."""


class WithoutEncryption(BaseModel):
    authorization_key: str
    """The raw authorization key data."""

    expires_at: float
    """The expiration time of the authorization key in seconds since the epoch."""

    wallets: List[Wallet]
    """The wallets that the signer has access to."""


WalletAuthenticateWithJwtResponse: TypeAlias = Union[WithEncryption, WithoutEncryption]
