# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .spark_transfer import SparkTransfer
from .spark_lightning_send_request import SparkLightningSendRequest

__all__ = ["SparkPayLightningInvoiceRpcResponse", "Data"]

Data: TypeAlias = Union[SparkTransfer, SparkLightningSendRequest]


class SparkPayLightningInvoiceRpcResponse(BaseModel):
    """Response to the Spark `payLightningInvoice` RPC."""

    method: Literal["payLightningInvoice"]

    data: Optional[Data] = None
    """A Spark transfer."""
