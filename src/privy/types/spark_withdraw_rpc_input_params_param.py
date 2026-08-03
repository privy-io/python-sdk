# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .spark_exit_speed import SparkExitSpeed

__all__ = ["SparkWithdrawRpcInputParamsParam"]


class SparkWithdrawRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `withdraw` RPC."""

    exit_speed: Required[SparkExitSpeed]
    """The exit speed for a cooperative withdrawal from Spark to L1."""

    onchain_address: Required[str]

    amount_sats: float

    deduct_fee_from_withdrawal_amount: bool

    fee_amount_sats: float

    fee_quote_id: str
