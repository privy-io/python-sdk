# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TronTransactionConditionField"]

TronTransactionConditionField: TypeAlias = Literal[
    "TransferContract.to_address",
    "TransferContract.amount",
    "TriggerSmartContract.contract_address",
    "TriggerSmartContract.call_value",
    "TriggerSmartContract.token_id",
    "TriggerSmartContract.call_token_value",
]
