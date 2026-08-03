# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ExternalTransactionWalletActionStepStatus"]

ExternalTransactionWalletActionStepStatus: TypeAlias = Literal[
    "preparing", "queued", "pending", "confirmed", "rejected", "failed"
]
