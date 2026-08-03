# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .typed_data_input import TypedDataInput
from .condition_operator import ConditionOperator

__all__ = ["EthereumTypedDataMessageCondition"]


class EthereumTypedDataMessageCondition(BaseModel):
    """
    'types' and 'primary_type' attributes of the TypedData JSON object defined in EIP-712.
    """

    field: str

    field_source: Literal["ethereum_typed_data_message"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    typed_data: TypedDataInput
    """
    The typed data structure containing EIP-712 types and the primary type for typed
    data message policy conditions.
    """

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
