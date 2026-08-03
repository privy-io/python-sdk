# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .embedded_wallet_recovery_method import EmbeddedWalletRecoveryMethod

__all__ = ["LinkedAccountSolanaEmbeddedWallet"]


class LinkedAccountSolanaEmbeddedWallet(BaseModel):
    """A Solana embedded wallet account linked to the user."""

    id: Optional[str] = None

    address: str

    chain_id: str

    chain_type: Literal["solana"]

    connector_type: Literal["embedded"]

    delegated: bool

    first_verified_at: Optional[float] = None

    imported: bool

    latest_verified_at: Optional[float] = None

    public_key: str

    recovery_method: EmbeddedWalletRecoveryMethod
    """The method used to recover an embedded wallet account."""

    type: Literal["wallet"]

    verified_at: float

    wallet_client: Literal["privy"]

    wallet_client_type: Literal["privy"]

    wallet_index: float
