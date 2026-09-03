# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AccountCreateResponse"]


class AccountCreateResponse(BaseModel):
    id: str

    account_type: str

    currency: str

    bank_name: Optional[str] = None

    last_4: Optional[str] = None
