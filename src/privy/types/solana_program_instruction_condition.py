# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator

__all__ = ["SolanaProgramInstructionCondition"]


class SolanaProgramInstructionCondition(BaseModel):
    """Solana Program attributes, enables allowlisting Solana Programs."""

    field: Literal["programId"]

    field_source: Literal["solana_program_instruction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
