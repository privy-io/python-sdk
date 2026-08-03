# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .hpke_encryption import HpkeEncryption

__all__ = ["WalletExportResponseBody"]


class WalletExportResponseBody(BaseModel):
    """Response body containing the encrypted wallet private key."""

    ciphertext: str
    """The encrypted private key."""

    encapsulated_key: str
    """
    The base64-encoded encapsulated key that was generated during encryption, for
    use during decryption.
    """

    encryption_type: HpkeEncryption
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""
