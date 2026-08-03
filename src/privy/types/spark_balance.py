# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel
from .spark_token_balance import SparkTokenBalance

__all__ = ["SparkBalance"]


class SparkBalance(BaseModel):
    """The balance of a Spark wallet."""

    balance: str

    token_balances: Dict[str, SparkTokenBalance]
