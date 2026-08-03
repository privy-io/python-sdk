# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spark_network import SparkNetwork

__all__ = ["SparkGetStaticDepositAddressRpcInputParam"]


class SparkGetStaticDepositAddressRpcInputParam(TypedDict, total=False):
    """Gets a static deposit address for the Spark wallet."""

    method: Required[Literal["getStaticDepositAddress"]]

    network: SparkNetwork
    """The Spark network."""
