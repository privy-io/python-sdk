# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EncryptedAuthorizationKey"]


class EncryptedAuthorizationKey(BaseModel):
    """HPKE-encrypted authorization key with encapsulated key and ciphertext."""

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
