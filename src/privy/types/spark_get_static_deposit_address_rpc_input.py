# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .spark_network import SparkNetwork

__all__ = ["SparkGetStaticDepositAddressRpcInput"]


class SparkGetStaticDepositAddressRpcInput(BaseModel):
    """Gets a static deposit address for the Spark wallet."""

    method: Literal["getStaticDepositAddress"]

    network: Optional[SparkNetwork] = None
    """The Spark network."""
