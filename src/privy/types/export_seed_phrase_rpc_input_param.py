# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .seed_phrase_export_input_param import SeedPhraseExportInputParam

__all__ = ["ExportSeedPhraseRpcInputParam"]


class ExportSeedPhraseRpcInputParam(TypedDict, total=False):
    """Exports the seed phrase of the wallet."""

    address: Required[str]

    method: Required[Literal["exportSeedPhrase"]]

    params: Required[SeedPhraseExportInputParam]
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""
