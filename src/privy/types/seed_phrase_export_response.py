# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .hpke_encryption import HpkeEncryption

__all__ = ["SeedPhraseExportResponse"]


class SeedPhraseExportResponse(BaseModel):
    """Response containing HPKE-encrypted wallet data (private key or seed phrase)."""

    ciphertext: str

    encapsulated_key: str

    encryption_type: HpkeEncryption
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""
