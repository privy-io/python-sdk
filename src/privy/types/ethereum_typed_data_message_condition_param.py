# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .typed_data_input_param import TypedDataInputParam

__all__ = ["EthereumTypedDataMessageConditionParam"]


class EthereumTypedDataMessageConditionParam(TypedDict, total=False):
    """
    'types' and 'primary_type' attributes of the TypedData JSON object defined in EIP-712.
    """

    field: Required[str]

    field_source: Required[Literal["ethereum_typed_data_message"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    typed_data: Required[TypedDataInputParam]
    """
    The typed data structure containing EIP-712 types and the primary type for typed
    data message policy conditions.
    """

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
