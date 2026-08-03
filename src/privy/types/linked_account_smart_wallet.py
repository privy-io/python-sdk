# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .smart_wallet_type import SmartWalletType

__all__ = ["LinkedAccountSmartWallet"]


class LinkedAccountSmartWallet(BaseModel):
    """A smart wallet account linked to the user."""

    address: str

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    smart_wallet_type: SmartWalletType
    """The supported smart wallet providers."""

    type: Literal["smart_wallet"]

    verified_at: float

    smart_wallet_version: Optional[str] = None
