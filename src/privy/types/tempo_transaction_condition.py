# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .tempo_transaction_condition_field import TempoTransactionConditionField

__all__ = ["TempoTransactionCondition"]


class TempoTransactionCondition(BaseModel):
    """A Tempo (type 118) transaction-level field.

    Evaluated once per transaction (not per call).
    """

    field: TempoTransactionConditionField
    """
    Tempo (type 118) transaction-level fields that can be referenced in a policy
    condition.
    """

    field_source: Literal["tempo_transaction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
