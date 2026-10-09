# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CryptoSearchConfigParams"]


class CryptoSearchConfigParams(TypedDict, total=False):
    q: Required[str]
    """Token symbol, name, or contract address in any chain format."""
