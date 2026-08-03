# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator

__all__ = ["ActionRequestBodyCondition"]


class ActionRequestBodyCondition(BaseModel):
    """Condition on the original wallet action API request body fields."""

    field: str

    field_source: Literal["action_request_body"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
