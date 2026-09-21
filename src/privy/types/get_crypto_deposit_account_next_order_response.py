# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .get_crypto_deposit_account_order_response import GetCryptoDepositAccountOrderResponse

__all__ = ["GetCryptoDepositAccountNextOrderResponse"]


class GetCryptoDepositAccountNextOrderResponse(BaseModel):
    """
    The next crypto deposit-account sweep into the path wallet after `after`, or null if none. The order object matches GET order.
    """

    order: Optional[GetCryptoDepositAccountOrderResponse] = None
    """A crypto deposit-account sweep identified by its wallet action ID.

    Status is the wallet-action status.
    """
