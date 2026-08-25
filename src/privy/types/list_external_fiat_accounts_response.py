# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .external_fiat_account import ExternalFiatAccount

__all__ = ["ListExternalFiatAccountsResponse"]


class ListExternalFiatAccountsResponse(BaseModel):
    """A list of external fiat accounts linked to a user."""

    accounts: List[ExternalFiatAccount]

    next_cursor: Optional[str] = None
