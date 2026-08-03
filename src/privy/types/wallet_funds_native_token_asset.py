# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WalletFundsNativeTokenAsset"]


class WalletFundsNativeTokenAsset(BaseModel):
    """A native token asset (e.g. ETH, SOL)."""

    address: None = None

    type: Literal["native-token"]
