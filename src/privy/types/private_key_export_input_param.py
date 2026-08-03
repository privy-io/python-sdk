# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .export_type import ExportType
from .hpke_encryption import HpkeEncryption
from .recipient_public_key import RecipientPublicKey

__all__ = ["PrivateKeyExportInputParam"]


class PrivateKeyExportInputParam(TypedDict, total=False):
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""

    encryption_type: Required[HpkeEncryption]
    """The encryption type of the wallet to import. Currently only supports `HPKE`."""

    recipient_public_key: Required[RecipientPublicKey]
    """
    The recipient public key for HPKE encryption, in PEM or DER (base64-encoded)
    format.
    """

    export_seed_phrase: bool

    export_type: ExportType
    """The export type.

    'display' is for showing the key to the user in the UI, 'client' is for
    exporting to the client application.
    """
