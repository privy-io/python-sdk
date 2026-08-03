# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .cross_app_smart_wallet import CrossAppSmartWallet
from .cross_app_embedded_wallet import CrossAppEmbeddedWallet

__all__ = ["LinkedAccountCrossApp"]


class LinkedAccountCrossApp(BaseModel):
    """A cross-app account linked to the user."""

    embedded_wallets: List[CrossAppEmbeddedWallet]

    first_verified_at: Optional[float] = None

    latest_verified_at: Optional[float] = None

    provider_app_id: str

    smart_wallets: List[CrossAppSmartWallet]

    subject: str

    type: Literal["cross_app"]

    verified_at: float
