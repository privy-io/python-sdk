# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["XrplSignTransactionRpcInputParamsParam"]


class XrplSignTransactionRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the XRPL `xrpl_signTransaction` RPC."""

    encoding: Required[Literal["hex"]]

    transaction: Required[str]
