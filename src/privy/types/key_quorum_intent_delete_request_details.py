# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .key_quorum_intent_delete_request_body import KeyQuorumIntentDeleteRequestBody

__all__ = ["KeyQuorumIntentDeleteRequestDetails"]


class KeyQuorumIntentDeleteRequestDetails(BaseModel):
    """Request details for deleting a key quorum via intent."""

    method: Literal["DELETE"]

    url: str

    body: Optional[KeyQuorumIntentDeleteRequestBody] = None
    """Empty request body for a key quorum delete intent."""
