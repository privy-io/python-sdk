# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkGetWithdrawalFeeQuoteRpcInputParamsParam"]


class SparkGetWithdrawalFeeQuoteRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `getWithdrawalFeeQuote` RPC."""

    amount_sats: Required[float]

    onchain_address: Required[str]
