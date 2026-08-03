# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator

__all__ = ["AggregationCondition"]


class AggregationCondition(BaseModel):
    """Condition referencing an aggregation value.

    The field must start with "aggregation." followed by the aggregation ID.
    """

    field: str

    field_source: Literal["reference"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
