# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .sui_transfer_objects_command_field import SuiTransferObjectsCommandField

__all__ = ["SuiTransferObjectsCommandCondition"]


class SuiTransferObjectsCommandCondition(BaseModel):
    """SUI TransferObjects command attributes, including recipient and amount fields."""

    field: SuiTransferObjectsCommandField
    """Supported fields for SUI TransferObjects command conditions.

    Only 'recipient' and 'amount' are supported.
    """

    field_source: Literal["sui_transfer_objects_command"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
