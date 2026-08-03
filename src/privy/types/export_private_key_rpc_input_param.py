# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .private_key_export_input_param import PrivateKeyExportInputParam

__all__ = ["ExportPrivateKeyRpcInputParam"]


class ExportPrivateKeyRpcInputParam(TypedDict, total=False):
    """Exports the private key of the wallet."""

    address: Required[str]

    method: Required[Literal["exportPrivateKey"]]

    params: Required[PrivateKeyExportInputParam]
    """Input for exporting a wallet (private key or seed phrase) with HPKE encryption."""
