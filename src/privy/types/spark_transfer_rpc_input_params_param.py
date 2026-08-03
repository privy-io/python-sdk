# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkTransferRpcInputParamsParam"]


class SparkTransferRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `transfer` RPC."""

    amount_sats: Required[float]

    receiver_spark_address: Required[str]
