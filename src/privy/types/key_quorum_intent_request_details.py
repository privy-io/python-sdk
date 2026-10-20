# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .key_quorum_update_request_body import KeyQuorumUpdateRequestBody

__all__ = ["KeyQuorumIntentRequestDetails"]


class KeyQuorumIntentRequestDetails(BaseModel):
    """Request details for a key quorum intent."""

    body: KeyQuorumUpdateRequestBody
    """Request input for updating an existing key quorum.

    At least one field must be provided.
    """

    method: Literal["PATCH"]

    url: str
