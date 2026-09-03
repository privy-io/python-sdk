# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PolicyCreateParams",
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
    "Owner",
    "OwnerUserID",
    "OwnerPublicKey",
]


class PolicyCreateParams(TypedDict, total=False):
    chain_type: Required[Literal["ethereum", "solana"]]
    """Chain type the policy applies to."""

    name: Required[str]
    """Name to assign to policy."""

    rules: Required[Iterable[Rule]]
    """The rules that apply to each method the policy covers."""

    version: Required[Literal["1.0"]]
    """Version of the policy. Currently, 1.0 is the only version."""

    owner: Optional[Owner]
    """The pem-formatted, P-256 public key of the owner of the policy.

    If you provide this, do not specify an owner_id as it will be generated
    automatically.
    """

    owner_id: Optional[str]
    """The key quorum ID to set as the owner of the policy.

    If you provide this, do not specify an owner.
    """

    privy_authorization_signature: Annotated[str, PropertyInfo(alias="privy-authorization-signature")]
    """Request authorization signature.

    If multiple signatures are required, they should be comma separated.
    """


class RuleConditionEthereumTransaction(TypedDict, total=False):
    field: Required[Literal["to", "value"]]

    field_source: Required[Literal["ethereum_transaction"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


class RuleConditionEthereumCalldata(TypedDict, total=False):
    abi: Required[object]

    field: Required[str]

    field_source: Required[Literal["ethereum_calldata"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


class RuleConditionEthereumTypedDataDomain(TypedDict, total=False):
    field: Required[Literal["chainId", "verifyingContract"]]

    field_source: Required[Literal["ethereum_typed_data_domain"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


class RuleConditionEthereumTypedDataMessageTypedDataType(TypedDict, total=False):
    name: Required[str]

    type: Required[str]


class RuleConditionEthereumTypedDataMessageTypedData(TypedDict, total=False):
    primary_type: Required[str]

    types: Required[Dict[str, Iterable[RuleConditionEthereumTypedDataMessageTypedDataType]]]


class RuleConditionEthereumTypedDataMessage(TypedDict, total=False):
    field: Required[str]

    field_source: Required[Literal["ethereum_typed_data_message"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    typed_data: Required[RuleConditionEthereumTypedDataMessageTypedData]

    value: Required[Union[str, List[str]]]


class RuleConditionEthereum7702Authorization(TypedDict, total=False):
    field: Required[Literal["contract"]]

    field_source: Required[Literal["ethereum_7702_authorization"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


class RuleConditionSolanaProgramInstruction(TypedDict, total=False):
    field: Required[Literal["programId"]]

    field_source: Required[Literal["solana_program_instruction"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


class RuleConditionSolanaSystemProgramInstruction(TypedDict, total=False):
    field: Required[Literal["instructionName", "Transfer.from", "Transfer.to", "Transfer.lamports"]]

    field_source: Required[Literal["solana_system_program_instruction"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


class RuleConditionSolanaTokenProgramInstruction(TypedDict, total=False):
    field: Required[
        Literal[
            "instructionName",
            "TransferChecked.source",
            "TransferChecked.destination",
            "TransferChecked.authority",
            "TransferChecked.amount",
            "TransferChecked.mint",
        ]
    ]

    field_source: Required[Literal["solana_token_program_instruction"]]

    operator: Required[Literal["eq", "gt", "gte", "lt", "lte", "in"]]

    value: Required[Union[str, List[str]]]


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


class Rule(TypedDict, total=False):
    action: Required[Literal["ALLOW", "DENY"]]
    """Action to take if the conditions are true."""

    conditions: Required[Iterable[RuleCondition]]
    """
    An unordered set of boolean conditions that define the action the rule allows or
    denies.
    """

    method: Required[
        Literal[
            "eth_sendTransaction",
            "eth_signTransaction",
            "eth_signTypedData_v4",
            "eth_sign7702Authorization",
            "signTransaction",
            "signAndSendTransaction",
            "exportPrivateKey",
            "*",
        ]
    ]
    """Method the rule applies to."""

    name: Required[str]
    """Name to assign to rule."""


class OwnerUserID(TypedDict, total=False):
    user_id: Required[str]


class OwnerPublicKey(TypedDict, total=False):
    public_key: Required[str]


Owner: TypeAlias = Union[OwnerUserID, OwnerPublicKey]
