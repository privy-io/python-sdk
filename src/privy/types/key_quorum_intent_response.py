# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .key_quorum import KeyQuorum
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .key_quorum_update_request_body import KeyQuorumUpdateRequestBody

__all__ = ["KeyQuorumIntentResponse", "KeyQuorumIntentResponseRequestDetails"]


class KeyQuorumIntentResponseRequestDetails(BaseModel):
    """
    The original key quorum update request that would be sent to the key quorum endpoint
    """

    body: KeyQuorumUpdateRequestBody
    """Request input for updating an existing key quorum.

    At least one field must be provided.
    """

    method: Literal["PATCH"]

    url: str


class KeyQuorumIntentResponse(BaseIntentResponse):
    """Response for a key quorum intent"""

    intent_type: Literal["KEY_QUORUM"]

    request_details: KeyQuorumIntentResponseRequestDetails
    """
    The original key quorum update request that would be sent to the key quorum
    endpoint
    """

    action_result: Optional[BaseActionResult] = None
    """
    Result of key quorum update execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[KeyQuorum] = None
    """A key quorum for authorizing wallet operations."""
