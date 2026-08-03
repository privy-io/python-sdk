# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .first_class_chain_type import FirstClassChainType
from .linked_account_base_wallet_type import LinkedAccountBaseWalletType

__all__ = ["LinkedAccountBaseWallet"]


class LinkedAccountBaseWallet(BaseModel):
    """Base schema for wallet accounts linked to the user."""

    address: str

    chain_type: FirstClassChainType
    """The wallet chain types that offer first class support."""

    type: LinkedAccountBaseWalletType
    """The type of wallet linked account (external wallet or smart wallet)."""
