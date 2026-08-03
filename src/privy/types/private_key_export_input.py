# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .export_type import ExportType
from .hpke_encryption import HpkeEncryption
from .recipient_public_key import RecipientPublicKey

__all__ = ["PrivateKeyExportInput"]


class PrivateKeyExportInput(BaseModel):
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""

    encryption_type: HpkeEncryption
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""

    recipient_public_key: RecipientPublicKey
    """
    The recipient public key for HPKE encryption, in PEM or DER (base64-encoded)
    format.
    """

    export_seed_phrase: Optional[bool] = None

    export_type: Optional[ExportType] = None
    """The export type.

    'display' is for showing the key to the user in the UI, 'client' is for
    exporting to the client application.
    """
