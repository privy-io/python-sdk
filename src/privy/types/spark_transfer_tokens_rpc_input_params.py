# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .spark_output_selection_strategy import SparkOutputSelectionStrategy
from .output_with_previous_transaction_data import OutputWithPreviousTransactionData

__all__ = ["SparkTransferTokensRpcInputParams"]


class SparkTransferTokensRpcInputParams(BaseModel):
    """Parameters for the Spark `transferTokens` RPC."""

    receiver_spark_address: str

    token_amount: float

    token_identifier: str

    output_selection_strategy: Optional[SparkOutputSelectionStrategy] = None
    """Strategy for selecting outputs in a Spark token transfer."""

    selected_outputs: Optional[List[OutputWithPreviousTransactionData]] = None
