# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam

__all__ = ["Ethereum7702AuthorizationConditionParam"]


class Ethereum7702AuthorizationConditionParam(TypedDict, total=False):
    """Allowed contract addresses for eth_sign7702Authorization requests."""

    field: Required[Literal["contract"]]

    field_source: Required[Literal["ethereum_7702_authorization"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
