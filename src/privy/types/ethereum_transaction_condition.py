# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .ethereum_transaction_condition_field import EthereumTransactionConditionField

__all__ = ["EthereumTransactionCondition"]


class EthereumTransactionCondition(BaseModel):
    """
    The verbatim Ethereum transaction object in an eth_signTransaction or eth_sendTransaction request.
    """

    field: EthereumTransactionConditionField
    """Ethereum transaction-level fields that can be referenced in a policy condition."""

    field_source: Literal["ethereum_transaction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
