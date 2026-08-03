# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .spark_network import SparkNetwork
from .spark_signing_keyshare import SparkSigningKeyshare

__all__ = ["SparkWalletLeaf"]


class SparkWalletLeaf(BaseModel):
    """A Spark wallet leaf node."""

    id: str

    network: SparkNetwork
    """The Spark network."""

    node_tx: str

    owner_identity_public_key: str

    refund_tx: str

    status: str

    tree_id: str

    value: float

    verifying_public_key: str

    vout: float

    parent_node_id: Optional[str] = None

    signing_keyshare: Optional[SparkSigningKeyshare] = None
    """A Spark signing keyshare."""
