# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .seed_phrase_export_response import SeedPhraseExportResponse

__all__ = ["ExportSeedPhraseRpcResponse"]


class ExportSeedPhraseRpcResponse(BaseModel):
    """Response to the `exportSeedPhrase` RPC."""

    data: SeedPhraseExportResponse
    """Response containing HPKE-encrypted wallet data (private key or seed phrase)."""

    method: Literal["exportSeedPhrase"]
