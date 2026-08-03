# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork
from .spark_create_lightning_invoice_rpc_input_params_param import SparkCreateLightningInvoiceRpcInputParamsParam

__all__ = ["SparkCreateLightningInvoiceRpcInputParam"]


class SparkCreateLightningInvoiceRpcInputParam(TypedDict, total=False):
    """Creates a Lightning invoice for the Spark wallet."""

    method: Required[Literal["createLightningInvoice"]]

    params: Required[SparkCreateLightningInvoiceRpcInputParamsParam]
    """Parameters for the Spark `createLightningInvoice` RPC."""

    network: SparkNetwork
    """The Spark network."""
