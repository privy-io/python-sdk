# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SolanaSignTransactionRpcInputParamsParam"]


class SolanaSignTransactionRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the SVM `signTransaction` RPC."""

    encoding: Required[Literal["base64"]]

    transaction: Required[str]
