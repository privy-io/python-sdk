# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TestAccount"]


class TestAccount(BaseModel):
    __test__ = False
    """A test account for an app."""
    id: str

    created_at: str

    email: str

    otp_code: str

    phone_number: str

    updated_at: str

    name: Optional[str] = None
