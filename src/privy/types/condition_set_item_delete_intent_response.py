# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .condition_set import ConditionSet
from .base_action_result import BaseActionResult
from .condition_set_item import ConditionSetItem
from .base_intent_response import BaseIntentResponse
from .condition_set_item_intent_delete_request_details import ConditionSetItemIntentDeleteRequestDetails

__all__ = ["ConditionSetItemDeleteIntentResponse"]


class ConditionSetItemDeleteIntentResponse(BaseIntentResponse):
    """Response for an intent that deletes a condition set item"""

    intent_type: Literal["CONDITION_SET_ITEM"]

    request_details: ConditionSetItemIntentDeleteRequestDetails
    """Request details for deleting a condition set item via intent."""

    action_result: Optional[BaseActionResult] = None
    """
    Result of condition set item execution (only present if status is 'executed' or
    'failed')
    """

    condition_set: Optional[ConditionSet] = None
    """A condition set for grouping related condition values."""

    current_resource_data: Optional[ConditionSetItem] = None
    """A single item in a condition set."""
