# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_set_item_intent_delete_request_body import ConditionSetItemIntentDeleteRequestBody

__all__ = ["ConditionSetItemIntentDeleteRequestDetails"]


class ConditionSetItemIntentDeleteRequestDetails(BaseModel):
    """Request details for deleting a condition set item via intent."""

    method: Literal["DELETE"]

    url: str

    body: Optional[ConditionSetItemIntentDeleteRequestBody] = None
    """Empty request body for a condition set item delete intent."""
