# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["SparkSigningKeyshare"]


class SparkSigningKeyshare(BaseModel):
    """A Spark signing keyshare."""

    owner_identifiers: List[str]

    public_key: str

    public_shares: Dict[str, str]

    threshold: float

    updated_time: str
