# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .intent_status import IntentStatus
from .intent_type_param import IntentTypeParam

__all__ = ["IntentListParams"]


class IntentListParams(TypedDict, total=False):
    created_by_id: str
    """Filter by creator user ID.

    For user-token requests, Privy uses the authenticated user ID to scope intent
    visibility. This filter only narrows that scoped result.
    """

    current_user_has_signed: Literal["true", "false"]

    cursor: str
    """Cursor returned by the previous page."""

    intent_type: IntentTypeParam
    """Type of intent."""

    limit: Optional[float]

    pending_member_id: str
    """Filter by a user whose approval is still pending.

    For user-token requests, Privy uses the authenticated user ID to scope intent
    visibility. This filter only narrows that scoped result.
    """

    resource_id: str

    sort_by: Literal["created_at_desc", "expires_at_asc", "updated_at_desc"]

    status: IntentStatus
    """Current status of an intent."""
