# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator
from .solana_token_program_instruction_condition_field import SolanaTokenProgramInstructionConditionField

__all__ = ["SolanaTokenProgramInstructionCondition"]


class SolanaTokenProgramInstructionCondition(BaseModel):
    """
    Solana Token Program attributes, including more granular TransferChecked instruction fields.
    """

    field: SolanaTokenProgramInstructionConditionField
    """
    Supported fields for Solana Token Program conditions including Transfer,
    TransferChecked, Burn, MintTo, CloseAccount, and InitializeAccount3 instruction
    fields.
    """

    field_source: Literal["solana_token_program_instruction"]

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
