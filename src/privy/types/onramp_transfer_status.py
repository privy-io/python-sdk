# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["OnrampTransferStatus"]

OnrampTransferStatus: TypeAlias = Literal[
    "awaiting_funds",
    "in_review",
    "funds_received",
    "payment_submitted",
    "payment_processed",
    "canceled",
    "error",
    "undeliverable",
    "returned",
    "refunded",
]
