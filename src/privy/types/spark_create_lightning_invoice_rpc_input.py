# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_create_lightning_invoice_rpc_input_params import SparkCreateLightningInvoiceRpcInputParams

__all__ = ["SparkCreateLightningInvoiceRpcInput"]


class SparkCreateLightningInvoiceRpcInput(BaseModel):
    """Creates a Lightning invoice for the Spark wallet."""

    method: Literal["createLightningInvoice"]

    params: SparkCreateLightningInvoiceRpcInputParams
    """Parameters for the Spark `createLightningInvoice` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
