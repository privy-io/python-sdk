# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AccountGetResponse", "Account"]


class Account(BaseModel):
    id: str

    account_type: str

    currency: str

    bank_name: Optional[str] = None

    last_4: Optional[str] = None


class AccountGetResponse(BaseModel):
    accounts: List[Account]
