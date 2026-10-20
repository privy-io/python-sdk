# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .key_quorum import KeyQuorum
from .base_action_result import BaseActionResult
from .base_intent_response import BaseIntentResponse
from .key_quorum_intent_request_details_union import KeyQuorumIntentRequestDetailsUnion

__all__ = ["KeyQuorumIntentResponse"]


class KeyQuorumIntentResponse(BaseIntentResponse):
    """Response for a key quorum intent"""

    intent_type: Literal["KEY_QUORUM"]

    request_details: KeyQuorumIntentRequestDetailsUnion
    """The original key quorum request. Method is PATCH (update) or DELETE (delete)."""

    action_result: Optional[BaseActionResult] = None
    """
    Result of key quorum execution (only present if status is 'executed' or
    'failed')
    """

    current_resource_data: Optional[KeyQuorum] = None
    """A key quorum for authorizing wallet operations."""
