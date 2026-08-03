# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .seed_phrase_export_input import SeedPhraseExportInput

__all__ = ["ExportSeedPhraseRpcInput"]


class ExportSeedPhraseRpcInput(BaseModel):
    """Exports the seed phrase of the wallet."""

    address: str

    method: Literal["exportSeedPhrase"]

    params: SeedPhraseExportInput
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""
