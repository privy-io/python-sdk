# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .condition_set import ConditionSet
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .condition_set_intent_delete_request_details import ConditionSetIntentDeleteRequestDetails

__all__ = ["ConditionSetDeleteIntentResponse"]


class ConditionSetDeleteIntentResponse(BaseIntentResponse):
    """Response for a condition set delete intent"""

    intent_type: Literal["CONDITION_SET"]

    request_details: ConditionSetIntentDeleteRequestDetails
    """Request details for deleting a condition set via intent."""

    action_result: Optional[BaseActionResult] = None
    """
    Result of condition set execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[ConditionSet] = None
    """A condition set for grouping related condition values."""
