# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .intent_type import IntentType
from .intent_status import IntentStatus

__all__ = ["IntentListParams"]


class IntentListParams(TypedDict, total=False):
    created_by_id: str

    current_user_has_signed: Literal["true", "false"]

    cursor: str

    intent_type: IntentType
    """Type of intent."""

    limit: Optional[float]

    pending_member_id: str

    resource_id: str

    sort_by: Literal["created_at_desc", "expires_at_asc", "updated_at_desc"]

    status: IntentStatus
    """Current status of an intent."""
