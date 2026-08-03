# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeStaticMemoDepositMetadata"]


class BridgeStaticMemoDepositMetadata(BaseModel):
    """Bridge metadata for a fiat deposit via static memo."""

    method: Literal["static_memo"]

    static_memo_event_id: str

    static_memo_id: str

    type: Literal["fiat_deposit"]
