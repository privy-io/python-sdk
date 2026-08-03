# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SparkCreateLightningInvoiceRpcInputParamsParam"]


class SparkCreateLightningInvoiceRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `createLightningInvoice` RPC."""

    amount_sats: Required[float]

    description_hash: str

    expiry_seconds: float

    include_spark_address: bool

    memo: str

    receiver_identity_pubkey: str
