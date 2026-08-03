# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam
from .solana_system_program_instruction_condition_field import SolanaSystemProgramInstructionConditionField

__all__ = ["SolanaSystemProgramInstructionConditionParam"]


class SolanaSystemProgramInstructionConditionParam(TypedDict, total=False):
    """
    Solana System Program attributes, including more granular Transfer instruction fields.
    """

    field: Required[SolanaSystemProgramInstructionConditionField]
    """
    Supported fields for Solana System Program conditions including Transfer
    instruction fields.
    """

    field_source: Required[Literal["solana_system_program_instruction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
