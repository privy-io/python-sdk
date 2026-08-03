# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_lightning_receive_request import SparkLightningReceiveRequest

__all__ = ["SparkCreateLightningInvoiceRpcResponse"]


class SparkCreateLightningInvoiceRpcResponse(BaseModel):
    """Response to the Spark `createLightningInvoice` RPC."""

    method: Literal["createLightningInvoice"]

    data: Optional[SparkLightningReceiveRequest] = None
    """A Spark Lightning receive request."""
