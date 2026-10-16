# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .condition_set_intent_delete_request_body import ConditionSetIntentDeleteRequestBody

__all__ = ["ConditionSetIntentDeleteRequestDetails"]


class ConditionSetIntentDeleteRequestDetails(BaseModel):
    """Request details for deleting a condition set via intent."""

    method: Literal["DELETE"]

    url: str

    body: Optional[ConditionSetIntentDeleteRequestBody] = None
    """Empty request body for a condition set delete intent."""
