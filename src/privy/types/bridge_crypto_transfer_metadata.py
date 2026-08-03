# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeCryptoTransferMetadata"]


class BridgeCryptoTransferMetadata(BaseModel):
    """Bridge metadata for a crypto deposit via transfer."""

    method: Literal["transfer"]

    source_wallet_address: str
    """The wallet address that sent the transfer."""

    transfer_id: str

    type: Literal["crypto_deposit"]
