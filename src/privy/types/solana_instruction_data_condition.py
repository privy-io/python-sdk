# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .solana_idl import SolanaIdl
from .condition_value import ConditionValue
from .condition_operator import ConditionOperator

__all__ = ["SolanaInstructionDataCondition"]


class SolanaInstructionDataCondition(BaseModel):
    """
    Solana instruction arguments and named accounts interpreted using an inline Anchor IDL.
    """

    field: str

    field_source: Literal["solana_instruction_data"]

    idl: SolanaIdl
    """
    A modern Anchor IDL containing selected instructions and their complete type
    dependencies.
    """

    operator: ConditionOperator
    """Operator to use for policy conditions."""

    value: ConditionValue
    """Value to compare against in a policy condition.

    Can be a single string or an array of strings.
    """
