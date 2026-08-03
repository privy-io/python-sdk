# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WalletActionStepType"]

WalletActionStepType: TypeAlias = Literal[
    "evm_transaction",
    "evm_user_operation",
    "svm_transaction",
    "tvm_transaction",
    "external_transaction",
    "custodian_transaction",
]
