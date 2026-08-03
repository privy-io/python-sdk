# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .spark_user_token_metadata import SparkUserTokenMetadata

__all__ = ["SparkTokenBalance"]


class SparkTokenBalance(BaseModel):
    """Balance of a Spark token."""

    balance: str

    token_metadata: SparkUserTokenMetadata
    """Metadata for a Spark user token."""
