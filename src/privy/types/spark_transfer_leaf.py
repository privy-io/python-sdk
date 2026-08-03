# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .spark_wallet_leaf import SparkWalletLeaf

__all__ = ["SparkTransferLeaf"]


class SparkTransferLeaf(BaseModel):
    """A Spark transfer leaf."""

    intermediate_refund_tx: str

    secret_cipher: str

    signature: str

    leaf: Optional[SparkWalletLeaf] = None
    """A Spark wallet leaf node."""
