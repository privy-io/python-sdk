# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .sui_transfer_objects_command_field import SuiTransferObjectsCommandField

__all__ = ["SuiTransferObjectsCommandConditionParam"]


class SuiTransferObjectsCommandConditionParam(TypedDict, total=False):
    """SUI TransferObjects command attributes, including recipient and amount fields."""

    field: Required[SuiTransferObjectsCommandField]
    """Supported fields for SUI TransferObjects command conditions.

    Only 'recipient' and 'amount' are supported.
    """

    field_source: Required[Literal["sui_transfer_objects_command"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
