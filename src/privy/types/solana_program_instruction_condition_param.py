# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam

__all__ = ["SolanaProgramInstructionConditionParam"]


class SolanaProgramInstructionConditionParam(TypedDict, total=False):
    """Solana Program attributes, enables allowlisting Solana Programs."""

    field: Required[Literal["programId"]]

    field_source: Required[Literal["solana_program_instruction"]]

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
