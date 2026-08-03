# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["IntentStatus"]

IntentStatus: TypeAlias = Literal["pending", "processing", "executed", "failed", "expired", "rejected", "dismissed"]
