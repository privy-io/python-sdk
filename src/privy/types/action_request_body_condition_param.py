# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam

__all__ = ["ActionRequestBodyConditionParam"]


class ActionRequestBodyConditionParam(TypedDict, total=False):
    """Condition on the original wallet action API request body fields."""

    field: Required[str]

    field_source: Required[Literal["action_request_body"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
