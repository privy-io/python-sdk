# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["BlockchainTransactionStatus"]

BlockchainTransactionStatus: TypeAlias = Literal[
    "broadcasted", "confirmed", "execution_reverted", "failed", "replaced", "finalized", "provider_error", "pending"
]
