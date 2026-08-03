# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .onramp_kyc_status import OnrampKYCStatus

__all__ = ["OnrampKYCResponse"]


class OnrampKYCResponse(BaseModel):
    """Response for an onramp KYC verification."""

    status: OnrampKYCStatus
    """Status of the KYC verification process."""

    user_id: str

    provider_user_id: Optional[str] = None
