# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EvmWalletActionStepStatus"]

EvmWalletActionStepStatus: TypeAlias = Literal[
    "preparing", "queued", "pending", "retrying", "confirmed", "rejected", "reverted", "replaced", "abandoned"
]
