# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkClaimStaticDepositRpcInputParamsParam"]


class SparkClaimStaticDepositRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `claimStaticDeposit` RPC."""

    credit_amount_sats: Required[float]

    signature: Required[str]

    transaction_id: Required[str]

    output_index: float
