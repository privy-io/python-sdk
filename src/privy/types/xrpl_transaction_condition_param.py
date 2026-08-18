# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .xrpl_transaction_condition_field import XrplTransactionConditionField

__all__ = ["XrplTransactionConditionParam"]


class XrplTransactionConditionParam(TypedDict, total=False):
    """Policy condition evaluated against decoded XRPL transaction fields."""

    field: Required[XrplTransactionConditionField]
    """Supported XRPL transaction field paths for policy conditions."""

    field_source: Required[Literal["xrpl_transaction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
