# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .ethereum_transaction_condition_field import EthereumTransactionConditionField

__all__ = ["EthereumTransactionConditionParam"]


class EthereumTransactionConditionParam(TypedDict, total=False):
    """
    The verbatim Ethereum transaction object in an eth_signTransaction or eth_sendTransaction request.
    """

    field: Required[EthereumTransactionConditionField]
    """Ethereum transaction-level fields that can be referenced in a policy condition."""

    field_source: Required[Literal["ethereum_transaction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
