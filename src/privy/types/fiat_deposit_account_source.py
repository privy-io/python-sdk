# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["FiatDepositAccountSource"]


class FiatDepositAccountSource(BaseModel):
    """
    The source fiat currency and available payment rails for a fiat deposit account.
    """

    currency: str

    payment_rails: List[str]
