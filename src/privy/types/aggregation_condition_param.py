# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam

__all__ = ["AggregationConditionParam"]


class AggregationConditionParam(TypedDict, total=False):
    """Condition referencing an aggregation value.

    The field must start with "aggregation." followed by the aggregation ID.
    """

    field: Required[str]

    field_source: Required[Literal["reference"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
