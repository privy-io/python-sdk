# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DerivationInputParam"]


class DerivationInputParam(TypedDict, total=False):
    """
    Derives the new wallet from an existing HD root wallet so both share one seed phrase.
    """

    wallet_id: Required[str]
    """ID of the HD root wallet to derive the new wallet from."""
