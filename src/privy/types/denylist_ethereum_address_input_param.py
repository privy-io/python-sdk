# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DenylistEthereumAddressInputParam"]


class DenylistEthereumAddressInputParam(TypedDict, total=False):
    """Denylist input for an Ethereum wallet address, which blocks SIWE logins."""

    type: Required[Literal["ethereumAddress"]]

    value: Required[str]
