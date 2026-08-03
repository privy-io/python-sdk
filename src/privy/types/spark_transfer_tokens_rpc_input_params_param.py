# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .spark_output_selection_strategy import SparkOutputSelectionStrategy
from .output_with_previous_transaction_data_param import OutputWithPreviousTransactionDataParam

__all__ = ["SparkTransferTokensRpcInputParamsParam"]


class SparkTransferTokensRpcInputParamsParam(TypedDict, total=False):
    """Parameters for the Spark `transferTokens` RPC."""

    receiver_spark_address: Required[str]

    token_amount: Required[float]

    token_identifier: Required[str]

    output_selection_strategy: SparkOutputSelectionStrategy
    """Strategy for selecting outputs in a Spark token transfer."""

    selected_outputs: Iterable[OutputWithPreviousTransactionDataParam]
