# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkPayLightningInvoiceRpcInputParamsParam"]


class SparkPayLightningInvoiceRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `payLightningInvoice` RPC."""

    invoice: Required[str]

    max_fee_sats: Required[float]

    amount_sats_to_send: float

    prefer_spark: bool
