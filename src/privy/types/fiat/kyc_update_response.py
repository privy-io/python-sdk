# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KYCUpdateResponse"]


class KYCUpdateResponse(BaseModel):
    status: Literal[
        "not_found",
        "active",
        "awaiting_questionnaire",
        "awaiting_ubo",
        "incomplete",
        "not_started",
        "offboarded",
        "paused",
        "rejected",
        "under_review",
    ]

    user_id: str

    provider_user_id: Optional[str] = None
