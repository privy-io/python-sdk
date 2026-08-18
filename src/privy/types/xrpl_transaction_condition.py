# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .xrpl_transaction_condition_field import XrplTransactionConditionField

__all__ = ["XrplTransactionCondition"]


class XrplTransactionCondition(BaseModel):
    """Policy condition evaluated against decoded XRPL transaction fields."""

    field: XrplTransactionConditionField
    """Supported XRPL transaction field paths for policy conditions."""

    field_source: Literal["xrpl_transaction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
