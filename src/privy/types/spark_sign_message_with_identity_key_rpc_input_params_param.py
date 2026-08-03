# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkSignMessageWithIdentityKeyRpcInputParamsParam"]


class SparkSignMessageWithIdentityKeyRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `signMessageWithIdentityKey` RPC."""

    message: Required[str]

    compact: bool
