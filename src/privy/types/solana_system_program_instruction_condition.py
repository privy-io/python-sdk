# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .solana_system_program_instruction_condition_field import SolanaSystemProgramInstructionConditionField

__all__ = ["SolanaSystemProgramInstructionCondition"]


class SolanaSystemProgramInstructionCondition(BaseModel):
    """
    Solana System Program attributes, including more granular Transfer instruction fields.
    """

    field: SolanaSystemProgramInstructionConditionField
    """
    Supported fields for Solana System Program conditions including Transfer
    instruction fields.
    """

    field_source: Literal["solana_system_program_instruction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
