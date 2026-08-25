# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .crypto_deposit_address_route import CryptoDepositAddressRoute

__all__ = ["CreateCryptoDepositAccountResponse"]


class CreateCryptoDepositAccountResponse(BaseModel):
    """Response returned after creating a crypto deposit account."""

    deposit_addresses: List[CryptoDepositAddressRoute]
