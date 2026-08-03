# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork

__all__ = ["SparkGetBalanceRpcInputParam"]


class SparkGetBalanceRpcInputParam(TypedDict, total=False):
    """Gets the balance of the Spark wallet."""

    method: Required[Literal["getBalance"]]

    network: SparkNetwork
    """The Spark network."""
