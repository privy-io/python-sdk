# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_pay_lightning_invoice_rpc_input_params import SparkPayLightningInvoiceRpcInputParams

__all__ = ["SparkPayLightningInvoiceRpcInput"]


class SparkPayLightningInvoiceRpcInput(BaseModel):
    """Pays a Lightning invoice from the Spark wallet."""

    method: Literal["payLightningInvoice"]

    params: SparkPayLightningInvoiceRpcInputParams
    """Parameters for the Spark `payLightningInvoice` RPC."""

    network: Optional[SparkNetwork] = None
    """The Spark network."""
