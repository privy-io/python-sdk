# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EthereumVaultPositionParams"]


class EthereumVaultPositionParams(TypedDict, total=False):
    vault_id: Required[str]
    """The vault ID to get position for."""

    include_archived: bool
    """Include archived wallets in lookup. Defaults to false."""
