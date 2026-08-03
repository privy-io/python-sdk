# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .test_account import TestAccount

__all__ = ["TestAccountsResponse"]


class TestAccountsResponse(BaseModel):
    __test__ = False
    """Response for listing test accounts for an app."""
    data: List[TestAccount]
