# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeFiatTransferMetadata"]


class BridgeFiatTransferMetadata(BaseModel):
    """Bridge metadata for a fiat deposit via transfer."""

    method: Literal["transfer"]

    transfer_id: str

    type: Literal["fiat_deposit"]
