# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .fiat_deposit_account import FiatDepositAccount

__all__ = ["ListFiatDepositAccountsResponse"]


class ListFiatDepositAccountsResponse(BaseModel):
    """A list of fiat deposit accounts linked to a wallet."""

    fiat_deposit_accounts: List[FiatDepositAccount]

    next_cursor: Optional[str] = None
