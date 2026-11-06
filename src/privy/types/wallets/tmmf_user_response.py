# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .tmmf_user_registration import TmmfUserRegistration
from .tmmf_user_wallet_response import TmmfUserWalletResponse

__all__ = ["TmmfUserResponse"]


class TmmfUserResponse(BaseModel):
    """
    A user's registration with each tMMF provider, and the wallets registered for each.
    """

    user_id: str
    """ID of the Privy user, which can be an organization."""

    user_registrations: List[TmmfUserRegistration]
    """The user's registrations with tMMF providers."""

    wallet_registrations: List[TmmfUserWalletResponse]
    """A page of wallets registered for the user with tMMF providers."""

    wallets_next_cursor: Optional[str] = None
    """Cursor of the next page of wallet registrations, or null on the last page."""
