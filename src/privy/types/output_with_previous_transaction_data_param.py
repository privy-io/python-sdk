# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .token_output_param import TokenOutputParam

__all__ = ["OutputWithPreviousTransactionDataParam"]


class OutputWithPreviousTransactionDataParam(TypedDict, total=False):
    """A Spark token output with its previous transaction data."""

    previous_transaction_hash: Required[str]

    previous_transaction_vout: Required[float]

    output: TokenOutputParam
    """A Spark token output."""
