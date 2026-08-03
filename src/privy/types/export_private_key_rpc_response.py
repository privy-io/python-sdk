# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .private_key_export_input import PrivateKeyExportInput

__all__ = ["ExportPrivateKeyRpcResponse"]


class ExportPrivateKeyRpcResponse(BaseModel):
    """Response to the `exportPrivateKey` RPC."""

    data: PrivateKeyExportInput
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""

    method: Literal["exportPrivateKey"]
