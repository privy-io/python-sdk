# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Policy",
    "Rule",
    "RuleCondition",
    "RuleConditionEthereumTransaction",
    "RuleConditionEthereumCalldata",
    "RuleConditionEthereumTypedDataDomain",
    "RuleConditionEthereumTypedDataMessage",
    "RuleConditionEthereumTypedDataMessageTypedData",
    "RuleConditionEthereumTypedDataMessageTypedDataType",
    "RuleConditionEthereum7702Authorization",
    "RuleConditionSolanaProgramInstruction",
    "RuleConditionSolanaSystemProgramInstruction",
    "RuleConditionSolanaTokenProgramInstruction",
]


class RuleConditionEthereumTransaction(BaseModel):
    field: Literal["to", "value"]

    field_source: Literal["ethereum_transaction"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


class RuleConditionEthereumCalldata(BaseModel):
    abi: object

    field: str

    field_source: Literal["ethereum_calldata"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


class RuleConditionEthereumTypedDataDomain(BaseModel):
    field: Literal["chainId", "verifyingContract"]

    field_source: Literal["ethereum_typed_data_domain"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


class RuleConditionEthereumTypedDataMessageTypedDataType(BaseModel):
    name: str

    type: str


class RuleConditionEthereumTypedDataMessageTypedData(BaseModel):
    primary_type: str

    types: Dict[str, List[RuleConditionEthereumTypedDataMessageTypedDataType]]


class RuleConditionEthereumTypedDataMessage(BaseModel):
    field: str

    field_source: Literal["ethereum_typed_data_message"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    typed_data: RuleConditionEthereumTypedDataMessageTypedData

    value: Union[str, List[str]]


class RuleConditionEthereum7702Authorization(BaseModel):
    field: Literal["contract"]

    field_source: Literal["ethereum_7702_authorization"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


class RuleConditionSolanaProgramInstruction(BaseModel):
    field: Literal["programId"]

    field_source: Literal["solana_program_instruction"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


class RuleConditionSolanaSystemProgramInstruction(BaseModel):
    field: Literal["instructionName", "Transfer.from", "Transfer.to", "Transfer.lamports"]

    field_source: Literal["solana_system_program_instruction"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


class RuleConditionSolanaTokenProgramInstruction(BaseModel):
    field: Literal[
        "instructionName",
        "TransferChecked.source",
        "TransferChecked.destination",
        "TransferChecked.authority",
        "TransferChecked.amount",
        "TransferChecked.mint",
    ]

    field_source: Literal["solana_token_program_instruction"]

    operator: Literal["eq", "gt", "gte", "lt", "lte", "in"]

    value: Union[str, List[str]]


RuleCondition: TypeAlias = Union[
    RuleConditionEthereumTransaction,
    RuleConditionEthereumCalldata,
    RuleConditionEthereumTypedDataDomain,
    RuleConditionEthereumTypedDataMessage,
    RuleConditionEthereum7702Authorization,
    RuleConditionSolanaProgramInstruction,
    RuleConditionSolanaSystemProgramInstruction,
    RuleConditionSolanaTokenProgramInstruction,
]


class Rule(BaseModel):
    id: str

    action: Literal["ALLOW", "DENY"]
    """Action to take if the conditions are true."""

    conditions: List[RuleCondition]
    """
    An unordered set of boolean conditions that define the action the rule allows or
    denies.
    """

    method: Literal[
        "eth_sendTransaction",
        "eth_signTransaction",
        "eth_signTypedData_v4",
        "eth_sign7702Authorization",
        "signTransaction",
        "signAndSendTransaction",
        "exportPrivateKey",
        "*",
    ]
    """Method the rule applies to."""

    name: str
    """Name to assign to rule."""


class Policy(BaseModel):
    id: str
    """Unique ID of the created policy.

    This will be the primary identifier when using the policy in the future.
    """

    chain_type: Literal["ethereum", "solana"]
    """Chain type the policy applies to."""

    created_at: float
    """Unix timestamp of when the policy was created in milliseconds."""

    name: str
    """Name to assign to policy."""

    owner_id: Optional[str] = None
    """The key quorum ID of the owner of the policy."""

    rules: List[Rule]
    """The rules that apply to each method the policy covers."""

    version: Literal["1.0"]
    """Version of the policy. Currently, 1.0 is the only version."""
