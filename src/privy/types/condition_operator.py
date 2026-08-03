# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ConditionOperator"]

ConditionOperator: TypeAlias = Literal[
    "eq", "gt", "gte", "lt", "lte", "in", "in_condition_set", "contains", "starts_with", "ends_with"
]
