# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["CardIssuingTransactionStatus"]

CardIssuingTransactionStatus: TypeAlias = Literal["pending", "posted", "declined", "expired", "reversed"]
