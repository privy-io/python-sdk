# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .tempo_transaction_condition_field import TempoTransactionConditionField

__all__ = ["TempoTransactionConditionParam"]


class TempoTransactionConditionParam(TypedDict, total=False):
    """A Tempo (type 118) transaction-level field.

    Evaluated once per transaction (not per call).
    """

    field: Required[TempoTransactionConditionField]
    """
    Tempo (type 118) transaction-level fields that can be referenced in a policy
    condition.
    """

    field_source: Required[Literal["tempo_transaction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
