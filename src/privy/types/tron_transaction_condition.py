# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .tron_transaction_condition_field import TronTransactionConditionField

__all__ = ["TronTransactionCondition"]


class TronTransactionCondition(BaseModel):
    """
    TRON transaction fields for TransferContract and TriggerSmartContract transaction types.
    """

    field: TronTransactionConditionField
    """
    Supported TRON transaction fields for TransferContract and TriggerSmartContract
    in format "TransactionType.field_name".
    """

    field_source: Literal["tron_transaction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
