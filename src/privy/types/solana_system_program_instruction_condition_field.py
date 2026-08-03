# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SolanaSystemProgramInstructionConditionField"]

SolanaSystemProgramInstructionConditionField: TypeAlias = Literal[
    "instructionName", "Transfer.from", "Transfer.to", "Transfer.lamports"
]
