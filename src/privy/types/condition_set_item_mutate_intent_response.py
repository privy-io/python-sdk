# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .condition_set import ConditionSet
from .base_action_result import BaseActionResult
from .condition_set_item import ConditionSetItem
from .base_intent_response import BaseIntentResponse
from .condition_set_item_intent_request_details import ConditionSetItemIntentRequestDetails

__all__ = ["ConditionSetItemMutateIntentResponse"]


class ConditionSetItemMutateIntentResponse(BaseIntentResponse):
    """Response for an intent that adds or replaces condition set items"""

    intent_type: Literal["CONDITION_SET_ITEM"]

    request_details: ConditionSetItemIntentRequestDetails
    """The original condition set item request.

    Method is POST (add items), PUT (replace items), or DELETE (delete an item)
    """

    action_result: Optional[BaseActionResult] = None
    """
    Result of condition set item execution (only present if status is 'executed' or
    'failed')
    """

    condition_set: Optional[ConditionSet] = None
    """A condition set for grouping related condition values."""

    current_resource_data: Optional[ConditionSetItem] = None
    """A single item in a condition set."""
