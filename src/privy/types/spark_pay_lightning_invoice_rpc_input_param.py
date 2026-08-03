# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_pay_lightning_invoice_rpc_input_params_param import SparkPayLightningInvoiceRpcInputParamsParam

__all__ = ["SparkPayLightningInvoiceRpcInputParam"]


class SparkPayLightningInvoiceRpcInputParam(TypedDict, total=False):
    """Pays a Lightning invoice from the Spark wallet."""

    method: Required[Literal["payLightningInvoice"]]

    params: Required[SparkPayLightningInvoiceRpcInputParamsParam]
    """Parameters for the Spark `payLightningInvoice` RPC."""

    network: SparkNetwork
    """The Spark network."""
