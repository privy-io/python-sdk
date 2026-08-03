# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .wallet import Wallet
from .._models import BaseModel

__all__ = ["WalletCreateWalletsWithRecoveryResponse"]


class WalletCreateWalletsWithRecoveryResponse(BaseModel):
    """The response from creating wallets with an associated recovery user."""

    recovery_user_id: str
    """The ID of the created user."""

    wallets: List[Wallet]
    """The wallets that were created."""
