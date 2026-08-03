# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CustodianTransactionWalletActionStepStatus"]

CustodianTransactionWalletActionStepStatus: TypeAlias = Literal[
    "preparing", "queued", "custodian_reviewing", "pending", "confirmed", "rejected", "failed"
]
