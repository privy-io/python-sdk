# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CryptoDepositAssetFilterAllParam"]


class CryptoDepositAssetFilterAllParam(TypedDict, total=False):
    """Match all assets."""

    mode: Required[Literal["all"]]
