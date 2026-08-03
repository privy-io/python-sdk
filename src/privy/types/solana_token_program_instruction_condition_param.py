# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .solana_token_program_instruction_condition_field import SolanaTokenProgramInstructionConditionField

__all__ = ["SolanaTokenProgramInstructionConditionParam"]


class SolanaTokenProgramInstructionConditionParam(TypedDict, total=False):
    """
    Solana Token Program attributes, including more granular TransferChecked instruction fields.
    """

    field: Required[SolanaTokenProgramInstructionConditionField]
    """
    Supported fields for Solana Token Program conditions including Transfer,
    TransferChecked, Burn, MintTo, CloseAccount, and InitializeAccount3 instruction
    fields.
    """

    field_source: Required[Literal["solana_token_program_instruction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
