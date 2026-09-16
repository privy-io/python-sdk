# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .crypto_deposit_address_route import CryptoDepositAddressRoute

__all__ = ["ListCryptoDepositAccountsResponse"]


class ListCryptoDepositAccountsResponse(BaseModel):
    """A page of active crypto deposit accounts for a destination wallet."""

    data: List[CryptoDepositAddressRoute]

    next_cursor: Optional[str] = None
