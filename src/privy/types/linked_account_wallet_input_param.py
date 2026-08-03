# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .first_class_chain_type import FirstClassChainType

__all__ = ["LinkedAccountWalletInputParam"]


class LinkedAccountWalletInputParam(TypedDict, total=False):
    """The payload for importing a wallet account."""

    address: Required[str]

    chain_type: Required[FirstClassChainType]
    """The wallet chain types that offer first class support."""

    type: Required[Literal["wallet"]]
