# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .hpke_encryption import HpkeEncryption

__all__ = ["WalletInitImportResponse"]


class WalletInitImportResponse(BaseModel):
    encryption_public_key: str
    """The base64-encoded encryption public key to encrypt the wallet entropy with."""

    encryption_type: HpkeEncryption
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""
