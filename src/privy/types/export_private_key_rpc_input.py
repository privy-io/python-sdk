# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .private_key_export_input import PrivateKeyExportInput

__all__ = ["ExportPrivateKeyRpcInput"]


class ExportPrivateKeyRpcInput(BaseModel):
    """Exports the private key of the wallet."""

    address: str

    method: Literal["exportPrivateKey"]

    params: PrivateKeyExportInput
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""
