# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SparkUserTokenMetadata"]


class SparkUserTokenMetadata(BaseModel):
    """Metadata for a Spark user token."""

    decimals: float

    max_supply: str

    raw_token_identifier: str

    token_name: str

    token_public_key: str

    token_ticker: str
