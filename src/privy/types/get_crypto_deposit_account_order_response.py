# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .wallets.wallet_action_status import WalletActionStatus

__all__ = ["GetCryptoDepositAccountOrderResponse"]


class GetCryptoDepositAccountOrderResponse(BaseModel):
    """A crypto deposit-account sweep identified by its wallet action ID.

    Status is the wallet-action status.
    """

    id: str
    """Wallet action ID of the deposit sweep."""

    status: WalletActionStatus
    """Status of a wallet action."""
