# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .solana_idl_param import SolanaIdlParam
from .condition_operator import ConditionOperator
from .condition_value_param import ConditionValueParam

__all__ = ["SolanaInstructionDataConditionParam"]


class SolanaInstructionDataConditionParam(TypedDict, total=False):
    """
    Solana instruction arguments and named accounts interpreted using an inline Anchor IDL.
    """

    field: Required[str]

    field_source: Required[Literal["solana_instruction_data"]]

    idl: Required[SolanaIdlParam]
    """
    A modern Anchor IDL containing selected instructions and their complete type
    dependencies.
    """

    operator: Required[ConditionOperator]
    """Operator to use for policy conditions."""

    value: Required[ConditionValueParam]
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
