# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DenylistSolanaAddressInputParam"]


class DenylistSolanaAddressInputParam(TypedDict, total=False):
    """Denylist input for a Solana wallet address, which blocks SIWS logins."""

    type: Required[Literal["solanaAddress"]]

    value: Required[str]
