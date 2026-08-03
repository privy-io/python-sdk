# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BridgeCryptoDepositMetadata"]


class BridgeCryptoDepositMetadata(BaseModel):
    """Bridge metadata for a crypto deposit via liquidation address."""

    drain_id: str

    liquidation_address: str
    """The crypto address of the liquidation address that received the deposit."""

    liquidation_address_id: str

    method: Literal["liquidation_address"]

    source_wallet_address: str
    """The address that sent the deposit."""

    type: Literal["crypto_deposit"]
