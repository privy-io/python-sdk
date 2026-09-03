# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FiatGetKYCLinkResponse", "RejectionReason"]


class RejectionReason(BaseModel):
    created_at: str

    developer_reason: str

    reason: str


class FiatGetKYCLinkResponse(BaseModel):
    id: str

    created_at: str

    customer_id: str

    email: str

    full_name: str

    kyc_link: str

    kyc_status: Literal[
        "not_started", "pending", "incomplete", "awaiting_ubo", "manual_review", "under_review", "approved", "rejected"
    ]

    rejection_reasons: List[RejectionReason]

    tos_link: str

    tos_status: Literal["pending", "approved"]

    persona_inquiry_type: Optional[str] = None
