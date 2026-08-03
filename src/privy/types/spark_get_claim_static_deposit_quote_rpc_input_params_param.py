# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkGetClaimStaticDepositQuoteRpcInputParamsParam"]


class SparkGetClaimStaticDepositQuoteRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `getClaimStaticDepositQuote` RPC."""

    transaction_id: Required[str]

    output_index: float
