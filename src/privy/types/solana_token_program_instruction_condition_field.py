# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SolanaTokenProgramInstructionConditionField"]

SolanaTokenProgramInstructionConditionField: TypeAlias = Literal[
    "instructionName",
    "Transfer.source",
    "Transfer.destination",
    "Transfer.authority",
    "Transfer.amount",
    "TransferChecked.source",
    "TransferChecked.destination",
    "TransferChecked.authority",
    "TransferChecked.amount",
    "TransferChecked.mint",
    "Burn.account",
    "Burn.mint",
    "Burn.authority",
    "Burn.amount",
    "MintTo.mint",
    "MintTo.account",
    "MintTo.authority",
    "MintTo.amount",
    "CloseAccount.account",
    "CloseAccount.destination",
    "CloseAccount.authority",
    "InitializeAccount3.account",
    "InitializeAccount3.mint",
    "InitializeAccount3.owner",
]
