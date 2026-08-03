# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .tron_transaction_condition_field import TronTransactionConditionField

__all__ = ["TronTransactionConditionParam"]


class TronTransactionConditionParam(TypedDict, total=False):
    """
    TRON transaction fields for TransferContract and TriggerSmartContract transaction types.
    """

    field: Required[TronTransactionConditionField]
    """
    Supported TRON transaction fields for TransferContract and TriggerSmartContract
    in format "TransactionType.field_name".
    """

    field_source: Required[Literal["tron_transaction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
