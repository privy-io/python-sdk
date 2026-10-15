# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .condition_set_items_request_body import ConditionSetItemsRequestBody

__all__ = ["ConditionSetItemIntentCreateRequestDetails"]


class ConditionSetItemIntentCreateRequestDetails(BaseModel):
    """Request details for adding items to a condition set via intent."""

    body: ConditionSetItemsRequestBody
    """Array of values to add to the condition set. Maximum 100 items per request."""

    method: Literal["POST"]

    url: str
