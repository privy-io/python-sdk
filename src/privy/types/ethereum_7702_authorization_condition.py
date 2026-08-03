# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator

__all__ = ["Ethereum7702AuthorizationCondition"]


class Ethereum7702AuthorizationCondition(BaseModel):
    """Allowed contract addresses for eth_sign7702Authorization requests."""

    field: Literal["contract"]

    field_source: Literal["ethereum_7702_authorization"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
